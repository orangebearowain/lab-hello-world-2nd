from dataclasses import dataclass
import yaml
import os

config_file = 'config.yaml'

if os.path.exists(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file) 
    if config is None:
        print("Error: YAML file is empty or couldn't be parsed.")
else:
    print(f"File '{config_file}' does not exist!")
    config = None  


@dataclass
class SmartThermo:
    name: str
    version: str
    features: list
    mode: str = "off"
    set_point: int = 72

    def output(self):
        features_str = ", ".join(self.features)  
        return f"Application: {self.name}\nVersion: {self.version}\nFeatures: {features_str}\nMode: {self.mode}\nSet Point: {self.set_point}"

    def change_mode(self, mode: bool):
        self.mode = mode
        print(f"Mode has been changed to {self.mode}")


    def update_temperature(self, temperature: int):
        self.set_point = temperature
        print(f"Temperature set point has been updated to {self.set_point}°F")

    def save_to_yaml(self):
        if os.path.exists(config_file):
            with open(config_file, 'r') as file:
                config = yaml.safe_load(file)

            vapp_config = config.get('vapp', {})
            vapp_config['mode'] = self.mode
            vapp_config['set_point'] = self.set_point
            config['vapp'] = vapp_config

            with open(config_file, 'w') as file:
                yaml.dump(config, file)
            print(f"Current state has been saved to {config_file}")
        else:
            print(f"Error: {config_file} does not exist, unable to save.")

if config:
    vapp_config = config.get('vapp', {})
    if not vapp_config:
        print("Error: 'vapp' configuration not found in the YAML file.")
    else:
        name = vapp_config.get('name', 'N/A')
        version = vapp_config.get('version', 'N/A')
        features = vapp_config.get('features', [])
        
        mode = vapp_config.get('mode', False) 
        
        set_point = vapp_config.get('set_point', 72)

        thermo_instance = SmartThermo(name=name, version=version, features=features, mode=mode, set_point=set_point)

        print(thermo_instance.output())

        thermo_instance.change_mode(True)  
        thermo_instance.update_temperature(75)  
        thermo_instance.save_to_yaml()  

    logging_config = config.get('logging', {})
    if not logging_config:
        print("Error: 'logging' configuration not found in the YAML file.")
    else:
        logging_level = logging_config.get('level', 'info')
        logging_file = logging_config.get('file', 'logs/output.log')


        print("\nLogging Configuration:")
        print(f"Logging Level: {logging_level}")
        print(f"Log File: {logging_file}")
