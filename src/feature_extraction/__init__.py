import logging

import extract_features
from definitions import RESOURCE_DIR
from resources import feature_templates, feature_schemas


__version__ = "1.0.0"
__all__ = [RESOURCE_DIR,  "extract_features"]

def initialize():
    print(f"Initializing feature-extraction v{__version__}")



logger = logging.Logger("Feature extraction")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


initialize()