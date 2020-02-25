import requests

def cloneSmartList (sl_id, cloned_name, folder_id, folder_type, description, token):

    authorization = "Bearer " + token
    url = "https://028-jjw-728.mktorest.com/rest/asset/v1/smartList/" + sl_id + "/clone.json"

    payload = 'name=' + cloned_name + '&folder={"id":' + folder_id +',"type":' + folder_type +'}&description='+ description
    print(payload)

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Authorization': authorization
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)