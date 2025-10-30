import connexion
from resources import aco_schemas, aco_templates
from src.aco import connexion


model = "llama3.2"
__all__=["connexion", "aco_schemas", "aco_templates", "model"]
