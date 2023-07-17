from functions import *
import yaml
import json

# Open the config.yml file and load its contents into the 'config' variable
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)


clientsId = getClientsId(config["apiKey"], config["networkId"])

clientsSplashAuthorizationStatuses = {"clientsSplashAuthorizationStatuses":[]}
for clientId in clientsId:
    splashAuthorizationStatus = getSplashAuthorizationStatus(config["apiKey"], config["networkId"], clientId)
    clientsSplashAuthorizationStatuses["clientsSplashAuthorizationStatuses"].append({"clientId":clientId, "splashAuthorizationStatus":splashAuthorizationStatus})

print(json.dumps(clientsSplashAuthorizationStatuses, indent=4))