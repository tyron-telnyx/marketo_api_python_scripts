import re
import urllib.parse

from Marketo_API_Get_Auth import getToken
from Marketo_API_Update_Email_Variable import postEmailVariable
from Marketo_API_Create_Email import postCreateEmail

base_url = 'https://028-jjw-728.mktorest.com'

token = getToken()
print(token)

# i = ['1662',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'FALSE',	'Leave your number porting headaches behind', 'Email Nurture Pre Sign Up MSP 05']
# template= i[0]
# fromName = i[1]
# fromAdd = i[2]
# replyAdd = i[3]
# operational = i[4]
# subject = i[5]
# name = i[6]
# response = postCreateEmail(template, name, "2539", fromName, fromAdd, replyAdd, operational, subject, token, base_url)

# response = '{"success":true,"errors":[],"requestId":"498f#1707981c612","warnings":[],"result":[{"id":4935,"name":"Email Nurture Pre Sign Up MSP 05","createdAt":"2020-02-24T23:21:53Z+0000","updatedAt":"2020-02-24T23:21:53Z+0000","url":"https://app-ab20.marketo.com/#EM4935A1LA1","subject":{"type":"Text","value":"Leave your number porting headaches behind"},"fromName":{"type":"Text","value":"Adroll Integration"},"fromEmail":{"type":"Text","value":"discover@telnyx.com"},"replyEmail":{"type":"Text","value":"discover@telnyx.com"},"folder":{"type":"Folder","value":2539,"folderName":"MSP"},"operational":false,"textOnly":false,"publishToMSI":false,"webView":false,"status":"draft","template":1662,"workspace":"Default","version":2,"autoCopyToText":true}]}'
# id = re.search('"id":(\d*),', response)
# print (id[1])

# utm = '?utm_source=mkto&utm_medium=email&utm_campaign=pre_sign_up_nurture_series_msp_01'
# utm = urllib.parse.quote(utm)
# print(utm)

variable_names=['img-Hero',	'text-Title',	'text-BodyText',	'title1-threeCol',	'text1-threeCol',	'img1-threeCol',	'title2-threeCol',	'text2-threeCol',	'img2-threeCol',	'title3-threeCol',	'text3-threeCol',	'img3-threeCol',	'title-twoCol',	'text-twoCol',	'textButton-twoCol',	'linkButton-twoCol',	'img-twoCol',	'text-BodyText2',	'utm']
module_ids = ['hero',	'title',	'bodyTextBlock',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'twoCol',	'twoCol',	'twoCol',	'twoCol',	'twoCol',	'bodyTextBlock2', ""	]
values = ['http://go.telnyx.com/rs/028-JJW-728/images/Email_Banner_MSPNurtureSeries01.png',	'Porting Made Simple With FastPort®',	'Port all your phone numbers in just a few clicks. Our easy-to-use portal and APIs streamline the process, providing absolute transparency from start to finish.',	'Stay In Control',	'Schedule, track and edit port requests with complete transparency',	'http://go.telnyx.com/rs/028-JJW-728/images/Email_Icon_Fastport%402x.png',	'Get Easy Access',	'Free, automated porting without having to deal with previous providers',	'http://go.telnyx.com/rs/028-JJW-728/images/Email_Icon_sip%402x.png',	'Grow And Scale',	'Extend your global reach - port phone numbers internationally',	'http://go.telnyx.com/rs/028-JJW-728/images/Email_Icon_24support%402x.png',	'Documo cut porting times by 40%',	'To enable customers to reliably transmit documents from anywhere, Documo turned to Telnyx for number and porting solutions that are built for scalable, enterprise-grade communications.',	'Read the case study',	'http://tlyx.co/cs-documo',	'http://go.telnyx.com/rs/028-JJW-728/images/Email_Image_MSP_factsheet_teaser%402x.png',	'Ready to start porting? Talk to our experts to get started. Happy Reading! The Telnyx Team',	'?utm_source=mkto&utm_medium=email&utm_campaign=pre_sign_up_nurture_series_msp_02']

email_id = "4935"

for i in range (0,len(variable_names)):

    variable_name = variable_names[i]
    value = urllib.parse.quote(values[i])
    module_id = module_ids[i]
    if module_id:
        postEmailVariable(email_id, variable_name, value, token, base_url, module_id)
    else:
        postEmailVariable(email_id, variable_name, value, token, base_url)

