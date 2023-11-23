# filename: data_ingestion/config_loader.py
import yaml

def load_config():
    """
    Loads the configuration from the config.yaml file.
    """
    with open('config/config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

# This function call is for testing purposes only
if __name__ == "__main__":
    config = load_config()
    print(config)