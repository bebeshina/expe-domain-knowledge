import json
from ast import literal_eval
from json import JSONDecodeError
import pandas as pd
import redis

from definitions import OUTPUT_DIR
from resources import rls_templates, rls_schemas
import ollama
import requests

# ----------------------------------- to improve, unsuccessful -------------------------------------------------------

def get_locution(text):
    prompt = rls_templates.locution_template.format(text=text)
    print("text>>>", text)
    response = ollama.generate(model='llama3.2',
                               prompt=prompt,
                               format=rls_schemas.LocutionRelations.model_json_schema()
                               )
    output = rls_schemas.LocutionRelations.model_validate_json(response.response)
    print(output)
    return output


def get_locution_test(texte, liste):
    prompt = rls_templates.locution_template.format(text=texte, lst=liste)
    response = ollama.chat(model='llama3.2',
                           format=rls_schemas.LocutionRelations.model_json_schema(),
                           messages=[{'role': 'system',
                                      'content': "A partir d'un terme du domaine automobile, il est demandé d'énumérer "
                                                 "les locutions, expressions ou mots composés qui contiennent ce terme."},
                                     {'role': 'user',
                                      'content': f"Voici le texte {texte} et une liste de termes {liste}.Donne moi les "
                                                 f"locutions ou des mots composés qui ontiennent ces termes"}],
                           options={
                               "temperature": 0.5,
                               "top_p": 0.4,
                               "top_k": 5,
                               "num_predict": 500
                           })
    output = rls_schemas.LocutionRelations.model_validate_json(response.message.content)
    print(output)
    return output


def get_locution_list(liste):
    resultat = []
    for terme in liste:
        prompt = f"A partir d'un terme du domaine automobile {terme}, il est demandé d'énumérer les mots composés qui contiennent ce terme."
        print(prompt)
        response = ollama.generate(model='llama3.2',
                                   prompt=prompt,
                                   format=rls_schemas.LocutionRelations.model_json_schema()
                                   )
        output = rls_schemas.LocutionRelations.model_validate_json(response.response)
        print(output)
        resultat.append(output)
    return resultat



    prompt = rls_templates.locution_template.format(lst=liste)
    response = ollama.chat(model='llama3.2',
                           format=rls_schemas.LocutionRelations.model_json_schema(),
                           messages=[{'role': 'system',
                                      'content': "A partir d'un terme du domaine automobile, il est demandé d'énumérer "
                                                 "les locutions, expressions ou mots composés qui contiennent ce terme."},
                                     {'role': 'user',
                                      'content': f"Voici une liste de termes {liste}. "}],
                           options={
                               "temperature": 0.5,
                               "top_p": 0.4,
                               "top_k": 5,
                               "num_predict": 500
                           })
    output = rls_schemas.LocutionRelations.model_validate_json(response.message.content)
    print(output)
# ---------------------------------------------------------------------------------------------------------------------
# (maybe filtering)

# with JDM, need to use reference

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
row = 0

def get_jdm_locutions(termes):
    params = {"types_ids": "11", "min_weight": 50}
    res = set()

    global row
    row += 1
    print(f"Processing row {row}")

    ts = literal_eval(termes)
    if ts:
        for terme in ts[0]:
            if terme in r.keys():
                print(f"Term in Redis {r.get(terme)}")
                lst = literal_eval(r.get(terme))
                print(lst)
                res.update(lst)
            else:
                try:
                    print("terme", terme)
                    response = requests.get("https://jdm-api.demo.lirmm.fr/v0/relations/from/{terme}?types_ids=11&min_weight=50".format(terme=terme), params=params)
                    js = response.json()
                    if "nodes" in js.keys():
                        locutions = [node["name"] for node in js["nodes"] if len(node["name"].split(" ")) < 4]
                        res.update(locutions)
                        r.set(terme,json.dumps(locutions))
                except JSONDecodeError:
                    r.set(terme, "['_']")
                    return json.dumps(["_"])
    print(res)
    upd = json.dumps(list(res))
    return upd


def replace_locutions_in_text(text, locs):
    if type(locs) != list:
        locutions = literal_eval(locs)
    else:
        locutions=locs
    locutions.extend(["mise à jour", "roues jumelées", "planches de surf", "jeux en ligne", "application embarquée",
                      "de verrouillage", "à encombrement réduit", "Frein de stationnement", "frein de stationnement",
                      "pavillon de toit", "Caméra de recul", "hybride rechargeable",  "charbon actif", "réglementation européenne",
                     "malus écologique", "fonction de bienvenue", "Poids à vide", "coffre de rangement", "appuie tête"])
    print(type(locutions))
    for locution in locutions:
        if len(locution.split(" ")) > 1:
            text = text.strip()
            if locution in text:
                text = text.replace(locution, locution.replace(" ", "_"))
                print(locution)
    return text


def get_year(year_str: str):
    if "2025" in year_str:
        return "25"
    elif "2024" in year_str:
        return "24"
    elif "2023" in year_str:
        return "23"
    else:
        return "other"


def run_replacement_in_text():
    raw = pd.read_csv(f"{OUTPUT_DIR}/data_mwt.csv", sep=";", encoding="utf8")
    raw["annee"] = raw["date"].apply(get_year)
    df = raw[raw["annee"] == "25"]
    df["updated_text"] = df.apply(lambda x: replace_locutions_in_text(x["stub"], x["locutions"]), axis=1)
    df.to_csv(f"{OUTPUT_DIR}/2025_mwt_loc.csv", sep=";", index=False)


def run():
    df = pd.read_csv(f"{OUTPUT_DIR}/data_with_nodes.csv", sep=";")
    r.set("Enyaq", "['_']")
    df["locutions"] = df["nouns"].apply(get_jdm_locutions)
    print(df.info())
    df.to_csv(f"{OUTPUT_DIR}/data_mwt_loc.csv", sep=";", index=False)


def drop_mwt_parts(toks, mwt):
    tokens = literal_eval(toks)[0]
    print(type(tokens))
    print(type(mwt))
    spl = []
    if mwt:
        for m in mwt:
            ts = m.split(" ")
            spl.extend(ts)
        print(spl)
        to_keep = [token for token in tokens if token not in spl]
        to_keep.extend(mwt)
        return to_keep
    else:
        return tokens


def get_available_mwts(s:str):
    mwts = [tok.replace("_", " ") for tok in s.split(" ") if "_" in tok]
    return mwts


def check():
    df = pd.read_csv(f"{OUTPUT_DIR}/2025_mwt_loc.csv", sep=";", encoding="utf8")
    df["present_mwt"] = df["updated_text"].apply(get_available_mwts)
    df["considered_tokens"] = df.apply(lambda x: drop_mwt_parts(x["nouns"], x["present_mwt"]), axis=1)
    df.to_csv(f"{OUTPUT_DIR}/data_mwt_loc_nodes.csv", sep=";", index=False)

