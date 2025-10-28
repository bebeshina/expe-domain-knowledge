from resources import rls_templates, rls_schemas
import ollama

from src import relation_extraction


def get_carac(text):
    prompt = rls_templates.manner_template.format(text=text)
    print("text>>>", text)
    response = ollama.generate(model=relation_extraction.model,
                               prompt=prompt,
                               format=rls_schemas.MannerRelations.model_json_schema()
                               )
    output = rls_schemas.MannerRelations.model_validate_json(response.response)
    print(output)
    return output