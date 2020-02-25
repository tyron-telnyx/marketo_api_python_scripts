import urllib.parse

from Marketo_API_Get_Auth import getToken
from Marketo_API_Update_Email_Variable import postEmailVariable

base_url = 'https://028-jjw-728.mktorest.com'

token = getToken()
print(token)

utm = '?utm_source=mkto&utm_medium=email&utm_campaign=pre_sign_up_nurture_series_msp_01'
utm = urllib.parse.quote(utm)
print(utm)

variable_names=['img-Hero',	'text-Title',	'text-BodyText',	'title1-threeCol',	'text1-threeCol',	'img1-threeCol',	'title2-threeCol',	'text2-threeCol',	'img2-threeCol',	'title3-threeCol',	'text3-threeCol',	'img3-threeCol',	'title-twoCol',	'text-twoCol',	'textButton-twoCol',	'linkButton-twoCol',	'img-twoCol',	'text-BodyText2',	'utm']
module_ids = ['hero',	'title',	'bodyTextBlock',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'threeCol',	'twoCol',	'twoCol',	'twoCol',	'twoCol',	'twoCol',	'bodyTextBlock2', ""	]
values=['http://go.telnyx.com/rs/028-JJW-728/images/Email_Banner_MSPNurtureSeries01.png',	'Telnyx provides the reliable voice services that you need',	'Telnyx voice solutions enable you to automate manual processes and streamline your customer experience',	'Automated Porting',	'Shorten porting time by weeks with FastPort.',	'http://go.telnyx.com/rs/028-JJW-728/images/Email_Icon_Fastport%402x.png',	'SIP Trunking',	'Scale communications with instant voice provisioning.',	'http://go.telnyx.com/rs/028-JJW-728/images/Email_Icon_sip%402x.png',	'24/7 Support',	'Team of in-house engineer support at no extra cost.',	'http://go.telnyx.com/rs/028-JJW-728/images/Email_Icon_24support%402x.png',	'Looking to Grow Your Business?',	'Learn how to leverage Telnyx to activate customers instantly, eliminate expensive engineering costs and collect actionable insights on your customers\' experiences.',	'Read the Fact Sheet',	'http://tlyx.co/fs-msp',	'http://go.telnyx.com/rs/028-JJW-728/images/Email_Image_MSP_factsheet_teaser%402x.png',	'Ready to start porting? Talk to our experts to get started.\nHappy Reading!\nThe Telnyx Team', utm]

email_id = "4934"

for i in range (0,19):

    variable_name = variable_names[i]
    value = values[i]
    module_id = module_ids[i]
    if module_id:
        postEmailVariable(email_id, variable_name, value, token, base_url, module_id)
    else:
        postEmailVariable(email_id, variable_name, value, token, base_url)

