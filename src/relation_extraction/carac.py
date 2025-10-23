import ollama
from definitions import RESOURCE_DIR
from resources import rls_templates, rls_schemas
from resources.rls_schemas import CaracRelations
from src import relation_extraction


def clean_output(output: CaracRelations):
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


def get_carac(text, nodes):
    prompt = rls_templates.carac_template.format(text=text, list=nodes)
    response = ollama.generate(model=relation_extraction.model,
                               prompt=prompt,
                               format=rls_schemas.CaracRelations.model_json_schema()
                               )
    output = rls_schemas.CaracRelations.model_validate_json(response.response)
    res = clean_output(output)
    # print("clean_relations >>>", res)
    return res
