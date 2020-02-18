import requests

response=requests.post('https://028-jjw-728.mktorest.com/rest/v1/leads/1446866/merge.json?access_token=5edd3cfc-2961-43cd-949a-db4c45c35ef1:ab',
					json=
					{
  "leadId": "1446867",
  "leadIds": ["1446867", "1446865"],
  "mergeInCRM": False,
})

print(response)
print(response.text)