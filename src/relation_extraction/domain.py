import json
from ast import literal_eval

import pandas as pd
import ollama
from definitions import OUTPUT_DIR
import redis


r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def determine_auto(term: str) -> int:
    # prompt = ("Return 1 if the term {term} is related to the automotive domain or to the car selling business "
    #           "otherwise return 0. "
    #           "Do not provide any explanation, code stub, text or comment, only return 1 or 0.".format(term=term))
    prompt = ("""<instruction>Pour le terme {term}
              - retourne 1 si le terme est lié au domaine automobile
              - retourne 0 si ce n'est pas le cas</instruction>
              <constraints>
              <constraint>Ne donne aucune explication ni commentaire.</constraint>
              <constraint>Ne propose pas de fonction. </constraint>
              <constraint>Retourne uniquement le résultat 1 ou 0.</constraint> """.format(term=term))

    response = ollama.generate(model='llama3.2',
                               prompt=prompt              )
    output = response.response
    print(term, output)
    return output


row = 0

def domain_sort_mwt(lst):
    if type(lst) != list:
        ls = json.loads(lst)
    else:
        ls = lst

    global row
    print(f"Processing row {row}")
    row += 1

    res = []
    print(len(ls))
    for t in ls:
        if f"d_{t}" in r.keys():
            res.append(int(r.get(f"d_{t}")))
        else:
            output = determine_auto(t)
            if output in [0, 1]:
                res.append(output)
                r.set(f"d_{t}", output)
            else:
                res.append(0)
                r.set(f"d_{t}", 0)

    print("Result", len(ls), len(res))
    if len(ls) == len(res):
        print(ls, res)
        return res
    else:
        print(ls, res)
        return []


def build_domain_vector():
    df = pd.read_csv(f"{OUTPUT_DIR}/data_mwt.csv", sep=";")
    sub = df[["locutions"]]
    print(sub.info())
    sub["auto_domain"] = sub["locutions"].apply(domain_sort_mwt)
    # sub.to_csv(f"{OUTPUT_DIR}/domain_data.csv", sep=";", index=False)


build_domain_vector()
