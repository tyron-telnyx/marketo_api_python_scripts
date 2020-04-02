import requests

def getLead (base_url, token, lead_id, fields):

    url = base_url + "/rest/v1/lead/"+lead_id+".json?fields=" + fields
    authorization = "Bearer " + token

    payload = {}
    headers = {
      'Authorization': authorization
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    return (response.text)
