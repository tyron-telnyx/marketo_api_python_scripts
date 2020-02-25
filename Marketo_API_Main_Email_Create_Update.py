import re
import urllib.parse

from Marketo_API_Get_Auth import getToken
from Marketo_API_Update_Email_Variable import postEmailVariable
from Marketo_API_Create_Email import postCreateEmail

base_url = 'https://028-jjw-728.mktorest.com'

token = getToken()
print(token)

i=['1671',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Save Money & Delight Your Customers', 'Email Nurture Pre Sign Up MSP 09']
template= i[0]
fromName = i[1]
fromAdd = i[2]
replyAdd = i[3]
operational = i[4]
subject = i[5]
name = i[6]
response = postCreateEmail(template, name, "2539", fromName, fromAdd, replyAdd, operational, subject, token, base_url)

#response = '{"success":true,"errors":[],"requestId":"498f#1707981c612","warnings":[],"result":[{"id":4935,"name":"Email Nurture Pre Sign Up MSP 05","createdAt":"2020-02-24T23:21:53Z+0000","updatedAt":"2020-02-24T23:21:53Z+0000","url":"https://app-ab20.marketo.com/#EM4935A1LA1","subject":{"type":"Text","value":"Leave your number porting headaches behind"},"fromName":{"type":"Text","value":"Adroll Integration"},"fromEmail":{"type":"Text","value":"discover@telnyx.com"},"replyEmail":{"type":"Text","value":"discover@telnyx.com"},"folder":{"type":"Folder","value":2539,"folderName":"MSP"},"operational":false,"textOnly":false,"publishToMSI":false,"webView":false,"status":"draft","template":1662,"workspace":"Default","version":2,"autoCopyToText":true}]}'
print(response)
email_id = re.search('"id":(\d*),', response)[1]
print (email_id)

variable_names=	['text-twoColHeader',	'textLink-twoColHeader',	'img-Hero',	'text-Title',	'',	'text-BodyText',	'title1-threeCol',	'text1-threeCol',	'img1-threeCol',	'title2-threeCol',	'text2-threeCol',	'img2-threeCol',	'title3-threeCol',	'text3-threeCol',	'img1-threeCol',	'img-ImageBlock',	'link-ImageBlock',	'text-BodyText2',	'text-BodyText3',	'utm']
module_ids=	['headerTwoCol',	'headerTwoCol',	'hero',	'title',	'',	'bodyTextBlock',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'imageBlock',	'imageBlock',	'bodyTextBlock2',	'bodyTextBlock3',	'']
values=	['Sign Up',	'https://telnyx.com/sign-up',	'',	'Grow your business efficiently with Telnyx',	'Hi {{lead.First Name}}',	'Cost reduction is a key priority for all businesses. In the managed services space, it’s particularly critical to provide a cost-competitive solution to clients. Companies have been able to realize significant cost savings and offer more competitive pricing, particularly as they scaled. Enable customers to make crystal clear calls  anywhere in the world, with improved reliability and redundancy over your current provider. A global IP network for more direct call connections and tighter security - this is telephony done right.',	'SIP Trunking',	'Scale communications with instant voice provisioning.',	'',	'FastPortⓇ',	'Get real-time CSR validation for faster, easier number porting',	'',	'24/7 Support',	'Our team of in-house engineers is available around the clock.',	'',	'http://go.telnyx.com/rs/028-JJW-728/images/Email_Image_teaser_missioncontrol%402x.png',	'https://telnyx.com/resources/demo-how-resellers-leverage-mission-control',	'Watch our short demo to get started on the Telnyx platform in minutes',	'Ready to start building? Talk to our experts. Happy watching, The Telnyx Team',	'?utm_source=mkto&utm_medium=email&utm_campaign=pre_sign_up_nurture_series_msp_09']

for i in range(0, len(variable_names)):
    variable_name = variable_names[i]
    value = urllib.parse.quote(values[i])
    module_id = module_ids[i]
    if module_id:
        postEmailVariable(email_id, variable_name, value, token, base_url, module_id)
    else:
        postEmailVariable(email_id, variable_name, value, token, base_url)

