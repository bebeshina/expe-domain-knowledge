import logging

from . import langchain_rdf_parser, langchain_rdf_vectorstore
from ..relation_extraction import loader
from definitions import CONFIG_PATH, INPUT_DIR, OUTPUT_DIR, RESOURCE_DIR, ONTOLOGY_DIR

# test,
__version__ = "1.2.0"
# "isa", "carac", "has_part", "test", "loader",
__all__ = ["langchain_rdf_parser", "langchain_rdf_vectorstore", CONFIG_PATH, INPUT_DIR, OUTPUT_DIR, RESOURCE_DIR, ONTOLOGY_DIR]

def initialize():
    print(f"Initializing ontology-parsing v{__version__}")


logger = logging.Logger("transcription")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


initialize()
