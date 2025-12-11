import json
import yaml
import sys
import os


try:
    path_argument = sys.argv[1]
except:
    print("Usage: python3 YAMLandJSONConverter.py <path>")
    sys.exit(1)

try:
    path = os.path.abspath(path_argument)

    if not os.path.exists(path):
        raise


    print("burası",path)
except:
    print("Invalid path")
    sys.exit(1)

if "json" in path:
    is_yaml = False
elif "yaml" in path:
    is_yaml = True
else:
    print("extension is not supported, only json or yaml file")
    sys.exit(1)


if is_yaml:
    try: 
        with open("python/config.yaml", "r") as yaml_file:
            data = yaml.safe_load(yaml_file)
    except Exception as e:
        print("Couldn't load YAML file!", e)
        sys.exit(1)


    try:
        with open("python/output.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print("Couldn't convert to json file", e)
        sys.exit(1)

else:

    try:
        with open("python/config.json", "r") as json_file:
            data = json.load(json_file)
    except Exception as e:
        print("Couldn't load YAML file!", e)
        sys.exit(1)


    try:
        with open("python/output.yaml", "w") as yaml_file:
            yaml.dump(data, yaml_file, indent=4)
    except Exception as e:
        print("Couldn't convert to YAML file", e)
        sys.exit(1)

    

    
    

print("Conversion completed")