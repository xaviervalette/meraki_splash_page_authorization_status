import requests

def getClientsId(token, networkId):

    url = f"https://api.meraki.com/api/v1/networks/{networkId}/clients"

    payload = None

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    clientsId = []
    for client in response.json():
        clientsId.append(client["id"])
    return clientsId

def getSplashAuthorizationStatus(token, networkId, clientId):
    url = f"https://api.meraki.com/api/v1/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus"

    payload = None

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    return response.json()

