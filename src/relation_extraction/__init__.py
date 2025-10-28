import logging
from . import loader, isa, syn, has_part, matter, carac, color, process, lieu
from definitions import CONFIG_PATH, INPUT_DIR, OUTPUT_DIR, RESOURCE_DIR
from resources import rls_templates, rls_schemas
model = "granite4"

__version__ = "1.1.0"


__all__ = ["loader",
           "isa",
           "syn",
           "has_part",
           "matter",
           "carac",
           "color",
           "process",
           "lieu",
           "rls_templates",
           "rls_schemas",
           CONFIG_PATH,
           INPUT_DIR,
           OUTPUT_DIR,
           RESOURCE_DIR,
           model]



def initialize():
    print(f"Initializing relation-extraction v{__version__}")


logger = logging.Logger("relation-extraction")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


initialize()
