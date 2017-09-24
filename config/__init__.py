import platform
from config.development import DevelopmentConfig
from config.production import ProductionConfig


def load_config():
    system = platform.system()
    if system == "Windows":
        return DevelopmentConfig
    elif system == "Linux":
        return ProductionConfig
