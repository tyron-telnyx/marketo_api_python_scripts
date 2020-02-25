import requests

def postApproveEmail(email_id, token):

    url = "https://028-jjw-728.mktorest.com/rest/asset/v1/email/"+email_id+"/approveDraft.json"
    authorization = "Bearer " + token

    payload = {}
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': authorization
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

    return (response.text.encode('utf8'))

