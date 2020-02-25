from Marketo_API_Get_Auth import getToken
from Marketo_API_Create_Email import postCreateEmail

base_url = 'https://028-jjw-728.mktorest.com'

token = getToken()
print(token)

email_content = [['1699',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Improve your telephony processes in minutes', 'Email Nurture Pre Sign Up MSP 02'],
['1697',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Compare Top Cloud Communication Platforms','Email Nurture Pre Sign Up MSP 03' ],
['1700',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Connectivity made simple with the Mission Control Portal', 'Email Nurture Pre Sign Up MSP 04'],
['1662',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Leave your number porting headaches behind', 'Email Nurture Pre Sign Up MSP 05'],
['1698',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Your competitors scale with Telnyx SIP Trunks', 'Email Nurture Pre Sign Up MSP 06'],
['1689',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Take control over your telephony stack', 'Email Nurture Pre Sign Up MSP 07'],
['1699',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Thousands of Businesses Use Telnyx ...', 'Email Nurture Pre Sign Up MSP 08'],
['1671',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Save Money & Delight Your Customers', 'Email Nurture Pre Sign Up MSP 09']]


for i in email_content:

    template= i[0]
    fromName = i[1]
    fromAdd = i[2]
    replyAdd = i[3]
    operational = i[4]
    subject = i[5]
    name = i[6]
    postCreateEmail(template, name, "2539", fromName, fromAdd, replyAdd, operational, subject, token, base_url)

