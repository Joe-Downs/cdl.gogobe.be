# Module used to get all the necessary information from config.ini
import configparser
config = configparser.ConfigParser()

config.read("config.ini")

def getDatabasePath():
    databasePath = config["General"]["Database"]
    return databasePath

def getGeneralLogPath():
    generalLog = config["General"]["LogFile"]
    return generalLog

def getLoggingLevel():
    loggingLevel = config["General"]["LogLevel"].upper()
    return loggingLevel

def getCommandPrefix():
    prefix = config["Bot"]["CommandPrefix"]
    return prefix

def getDiscordToken():
    token = config["Bot"]["DiscordToken"]
    return token

def getBotLogPath():
    botLog = config["Bot"]["LogFile"]
    return botLog

def getWebLogPath():
    webLog = config["Website"]["LogFile"]
    return botLog

def getWebHomeDir():
    webHome = config["Website"]["HomeDirectory"]
    return webHome
