import requests

def postCreateEmail(template_id, email_name, folder_id, from_name, from_add, reply_add, operational, subject, token, base_url, folder_type):

    url = base_url + "/rest/asset/v1/emails.json"
    authorization = "Bearer " + token

    payload = 'folder={"id":' + folder_id+',"type":'+folder_type + '}&template=' + template_id + '&subject=' + subject + '&fromName=' + from_name + '&fromEmail=' + from_add + '&replyEmail=' + reply_add + '&operational=' + operational + '&name=' + email_name
    print(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': authorization
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

    return (response.text)

