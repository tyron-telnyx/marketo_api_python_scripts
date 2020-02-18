import requests
import re

def getToken ():
    response = requests.get('https://028-jjw-728.mktorest.com/identity/oauth/token?grant_type=client_credentials&client_id=2d590650-c448-48ea-8f94-dbc8170a741c&client_secret=No0QXGn3dCtITnF7jRM1FYUuHD5703pa')

    print(response)
    print(response.text)

    token = re.search('access_token":"(.*)","token_type"', response.text)
    print(token.group(1))

    return token.group(1)

getToken()