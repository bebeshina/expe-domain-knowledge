import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.yml')
RESOURCE_DIR = os.path.join(ROOT_DIR, "resources")
ONTOLOGY_DIR = os.path.join(ROOT_DIR, "ontologies")
VECTORSTORE_DIR = os.path.join(ROOT_DIR, "chroma")
INPUT_DIR = os.path.join(ROOT_DIR, 'data/input')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'data/output')


