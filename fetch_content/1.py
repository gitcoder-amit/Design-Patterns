import json


def parse_config(config):
    config_dict = {}
    # print(config.splitlines())
    for line in config.splitlines():
        # print(line)
        line = line.strip()
        if line and not line.startswith('#'):
            key, value = line.split('=', 1)
            config_dict[key.strip()] = value.strip()
    return config_dict

# Parsing the configuration content
config_content = """
# Configuration File
# This is a sample configuration file
# Comments start with a hash symbol '#'

database_host = localhost
database_port = 5432
database_name = mydb
database_username = admin
database_password = pswrd
# database_password = password123
database_host = 127.0.0.1"""
config_dict = parse_config(config_content)
print(config_dict)


# Preparing the final dictionary with selected keys
final_config = {
    "database_port": config_dict.get("database_port"),
    "database_password": config_dict.get("database_password"),
    "database_host": config_dict.get("database_host"),
}

# Converting the final dictionary to JSON format
final_config_json = json.dumps(final_config, indent=4)
print(final_config_json)