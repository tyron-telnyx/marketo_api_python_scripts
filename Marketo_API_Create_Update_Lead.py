import requests
import json

def createUpdateLead(base_url, token, lead_list):

    url = base_url + '/rest/v1/leads.json'
    payload = {
   "action":"updateOnly",
   "lookupField":"id",
   "input": lead_list
}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    return (response.text)

#createUpdateLead('https://028-jjw-728.mktorest.com', '047596fa-5778-4fe3-a2eb-65b1d9878eb2:ab', [])