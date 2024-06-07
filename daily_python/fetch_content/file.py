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

# Reading the configuration file
file_path = 'path/to/your/db_config.txt'
with open(file_path, 'r') as file:
    config_content = file.read()

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
