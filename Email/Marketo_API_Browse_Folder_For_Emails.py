import requests

def getEmailbyBrowse (max_return, folder_id, folder_type, token):
    authorization = "Bearer " + token

    url = 'https://028-jjw-728.mktorest.com/rest/asset/v1/emails.json?maxReturn=' + max_return + '&folder={\"id\":' + folder_id + ',\"type\":\"' + folder_type +'\"}'

    payload = {}
    headers = {
      'Authorization': authorization
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    # print(response.text.encode('utf8'))

    return response