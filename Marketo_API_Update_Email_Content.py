import requests
import urllib.parse


def postEmailContent(email_id, html_id, type, value, text_value, token):

    url = "https://028-jjw-728.mktorest.com/rest/asset/v1/email/"+email_id+"/content/"+html_id+".json"
    authorization = "Bearer " + token
    payload = 'type=' + type + '&value='+value+'&textValue=' + text_value
    # payload = urllib.parse.quote(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': authorization
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

    return (response.text.encode('utf8'))

