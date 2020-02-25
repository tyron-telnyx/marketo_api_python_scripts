import requests

def postEmailVariable(email_id, variable_name, value, token, base_url, *optional):

    url = base_url + "/rest/asset/v1/email/"+email_id+"/variable/"+variable_name+".json"
    authorization = "Bearer " + token
    if optional:
        payload = 'value='+value +'&moduleId=' + optional[0]
        print(payload)
    else:
        payload = 'value=' + value
        print(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': authorization
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

    return (response.text.encode('utf8'))

