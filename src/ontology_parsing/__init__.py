import logging

from . import test, langchain_rdf_parser, langchain_rdf_vectorstore
from ..relation_extraction import loader
from definitions import CONFIG_PATH, INPUT_DIR, OUTPUT_DIR, RESOURCE_DIR, ONTOLOGY_DIR


__version__ = "1.0.0"
# "isa", "carac", "has_part",
__all__ = ["test", "loader", "langchain_rdf_parser", "langchain_rdf_vectorstore", CONFIG_PATH, INPUT_DIR, OUTPUT_DIR, RESOURCE_DIR, ONTOLOGY_DIR]

def initialize():
    print(f"Initializing relation-extraction v{__version__}")


logger = logging.Logger("transcription")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


initialize()
