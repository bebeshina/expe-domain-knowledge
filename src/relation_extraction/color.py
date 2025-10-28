import ollama

from resources import rls_templates, rls_schemas
from resources.rls_schemas import ColorRelations


def clean_output(output: ColorRelations):
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



def get_color(text, liste):
    prompt = rls_templates.color_template.format(text=text, list=liste)
    # print("text>>>", text)
    # print("liste>>>", liste)
    response = ollama.generate(model='llama3.2',
                               prompt=prompt,
                               format=rls_schemas.HasPartRelations.model_json_schema()
                               )
    output = rls_schemas.ColorRelations.model_validate_json(response.response)
    res = clean_output(output)
    # print("clean_relations >>>", res)
    return res


