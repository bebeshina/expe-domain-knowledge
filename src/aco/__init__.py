import connexion, associations
from resources import aco_schemas, aco_templates, extraction_templates
from src.aco import connexion
import ollama

model = "llama3.2"
__all__=["connexion", "associations", "aco_schemas", "aco_templates", "model", "ollama", "extraction_templates"]
