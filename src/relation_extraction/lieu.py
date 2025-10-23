import ollama

from resources import rls_templates, rls_schemas
from resources.rls_schemas import LieuRelations
from src import relation_extraction


def clean_output(output: LieuRelations):
    rels = output.relations
    result = []
    if rels:
        for d in rels:
            source = d.source
            cible = d.cible
            if source.casefold() != cible.casefold():
                if source not in cible:
                    if cible != "":
                        result.append(d)
    return result



def get_lieu(text, liste):
    prompt = rls_templates.lieu_template.format(text=text, list=liste)
    # print("text>>>", text)
    # print("liste>>>", liste)
    response = ollama.generate(model=relation_extraction.model,
                               prompt=prompt,
                               format=rls_schemas.LieuRelations.model_json_schema()
                               )
    output = rls_schemas.LieuRelations.model_validate_json(response.response)
    res = clean_output(output)
    # print("clean_relations >>>", res)
    return res