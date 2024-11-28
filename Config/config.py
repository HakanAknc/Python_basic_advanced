import configparser

class Config:
    def __init__(self, config_file='Config/config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, section, option):
        """Bir değeri string olarak alır."""
        return self.config.get(section, option)

    def get_boolean(self, section, option):
        """Bir değeri bool olarak alır."""
        return self.config.getboolean(section, option)
