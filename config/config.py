# filename: config/config.py
import yaml

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        with open('config/config.yaml', 'r') as config_file:
            self.config_data = yaml.safe_load(config_file)

    def get(self, key, default=None):
        return self.config_data.get(key, default)

# Example usage:
# config = Config()
# database_config = config.get('database')