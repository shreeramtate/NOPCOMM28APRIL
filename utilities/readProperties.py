import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getUsername():
        useremail=config.get('common info','username')
        return useremail


    @staticmethod
    def getPassword():
        Password = config.get('common info', 'password')
        return Password

