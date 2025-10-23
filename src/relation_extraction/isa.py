from typing import List

import ollama
from definitions import RESOURCE_DIR
from resources import rls_templates, rls_schemas
from resources.rls_schemas import IsaRelations

from src import relation_extraction


# @todo suggestion and validation agents


def clean_output(output: IsaRelations):
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


def get_isa(text, liste):
    prompt = rls_templates.isa_template.format(text=text, list=liste)
    # print("text>>>", text)
    # print("liste>>>", liste)
    # lllama3.2
    response = ollama.generate(model=relation_extraction.model,
                               prompt=prompt,
                               format=rls_schemas.IsaRelations.model_json_schema()
                               )
    output = rls_schemas.IsaRelations.model_validate_json(response.response)

    res = clean_output(output)
    # print("clean_relations >>>", res)
    return res



def run():
    df = relation_extraction.loader.get_texts()[:20]
    df["isa"] = df["text"].apply(get_isa)
    print(df["isa"])


# run()

