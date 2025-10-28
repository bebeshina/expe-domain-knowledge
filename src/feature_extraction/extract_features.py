import ollama
from resources import feature_templates, feature_schemas


def get_model_features(text):
    prompt = feature_templates.model_template.format(text=text)
    print("model>>>", text)
    response = ollama.generate(model='llama3.2',
                               prompt=prompt,
                               format=feature_schemas.CarModel.model_json_schema()
                               )
    output = feature_schemas.CarModel.model_validate_json(response.response)
    print(output)
    return output


get_model_features("Audi A1")