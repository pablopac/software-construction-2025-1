import configparser

class ConfigLoader:
    @staticmethod
    def load_credentials(tag, file_path="db_credentials.ini"):
        config = configparser.ConfigParser()
        config.read(file_path)
        return config[tag]["user"], config[tag]["password"]





