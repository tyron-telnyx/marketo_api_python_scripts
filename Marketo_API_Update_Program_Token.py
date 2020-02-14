import requests

def updateProgramToken (token_name, token_value, token_type, folder_id, folder_type, token):

    authorization = "Bearer " + token
    url = "https://028-jjw-728.mktorest.com/rest/asset/v1/folder/" + folder_id + "/tokens.json"

    payload = 'name=' + token_name + '&value=' + token_value + '&type=' + token_type + '&folderType=' + folder_type

    print(payload)

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Authorization': authorization
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)