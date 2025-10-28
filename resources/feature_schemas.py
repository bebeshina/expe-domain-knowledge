from pydantic import BaseModel

# traiter chaque feature séparemment


class CarModel(BaseModel):
    """
    à partir du nom de modèle, récupérer ses caractéristiques (features)
    """
    name: str
    engine: str
    model_dimensions_cm: str
    trunk_capacity_l: str
    type: str
    similar_models: list



