import requests
import json

# Function to parse the config file content
def parse_config(config):
    config_dict = {}
    for line in config.splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            key, value = line.split('=', 1)
            config_dict[key.strip()] = value.strip()
    return config_dict

# URL of the config file
url = "https://storage.googleapis.com/backend_resources_spotdraft/Iterview%20Questions/Config%20File%20Parser%20db_config.txt"

# Fetching the content of the file
response = requests.get(url)
config_content = response.text

# Parsing the configuration content
config_dict = parse_config(config_content)

# Preparing the final dictionary with selected keys
final_config = {
    "database_port": config_dict.get("database_port"),
    "database_password": config_dict.get("database_password"),
    "database_host": config_dict.get("database_host"),
}

# Converting the final dictionary to JSON format
final_config_json = json.dumps(final_config, indent=4)
print(final_config_json)
