import requests


def createUpdateLead(base_url, token, lead_list):

    url = base_url + '/rest/v1/leads.json'

    payload = {
        "action": "updateOnly",
        "lookupField": "id",
        "input": lead_list
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return (response.text)