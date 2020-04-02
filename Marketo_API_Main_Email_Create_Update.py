import re
import urllib.parse

from Marketo_API_Get_Auth import getToken
from Marketo_API_Update_Email_Variable import postEmailVariable
from Marketo_API_Create_Email import postCreateEmail
from Marketo_API_Update_Email_Content import postEmailContent

base_url = 'https://028-jjw-728.mktorest.com'

token = getToken()
print(token)

# i=['1818',	'Team Telnyx',	'discover@telnyx.com',	'discover@telnyx.com',	'Scale with Enterprise-grade Telephony',	'EM - March Dev 2020',	'2058',	'"Program"']
# template= i[0]
# fromName = i[1]
# fromAdd = i[2]
# replyAdd = i[3]
# operational = "FALSE"
# subject = i[4]
# name = i[5]
# folder_type = i[7]
# folder_id = i[6]
# response = postCreateEmail(template, name, folder_id, fromName, fromAdd, replyAdd, operational, subject, token, base_url, folder_type)
#
# #response = '{"success":true,"errors":[],"requestId":"498f#1707981c612","warnings":[],"result":[{"id":4935,"name":"Email Nurture Pre Sign Up MSP 05","createdAt":"2020-02-24T23:21:53Z+0000","updatedAt":"2020-02-24T23:21:53Z+0000","url":"https://app-ab20.marketo.com/#EM4935A1LA1","subject":{"type":"Text","value":"Leave your number porting headaches behind"},"fromName":{"type":"Text","value":"Adroll Integration"},"fromEmail":{"type":"Text","value":"discover@telnyx.com"},"replyEmail":{"type":"Text","value":"discover@telnyx.com"},"folder":{"type":"Folder","value":2539,"folderName":"MSP"},"operational":false,"textOnly":false,"publishToMSI":false,"webView":false,"status":"draft","template":1662,"workspace":"Default","version":2,"autoCopyToText":true}]}'
# print(response)
# email_id = re.search('"id":(\d*),', response)[1]
# print (email_id)

email_id = "4979"

# variable_names=	['link-Feature',	'src-Feature',	'title-FeatureBlock',	'text-FeatureBlock',	'cardLinkIn',	'cardSourceIn',	'cardTitleIn',	'cardTextIn',	'cardLinkIn',	'cardSourceIn',	'cardTitleIn',	'cardTextIn']
# module_ids=	['featureImgM',	'featureImgM',	'bodyTextBlock2',	'bodyTextBlock2',	'cardIn',	'cardIn',	'cardIn',	'cardIn',	'cardIn2',	'cardIn2',	'cardIn2',	'cardIn2']
# values=	['https://telnyx.com/resources/send-sms-with-the-telnyx-python-sdk',	'http://go.telnyx.com/rs/028-JJW-728/images/Asset_Email_Image_badal_videotease%402x.png',	'Send Your First SMS Using the Python SDK',	'In this guide, messaging engineer Badal M. will walk through sending your first SMS using our Python SDK',	'https://telnyx.com/resources/using-telnyx-call-control-for-conferencing',	'http://go.telnyx.com/rs/028-JJW-728/images/Asset_Email_Thumbnail_paul_videotease%402x.png',	'Using Call Control for Conferencing',	'Learn about how to use Telnyx Call Control to build your conferencing solution. Read our quick guide to creating a conference with node.js.',	'https://telnyx.com/resources/using-telnyx-call-control-for-conferencing',	'http://go.telnyx.com/rs/028-JJW-728/images/Asset_Email_Thumbnail_rip-pipenv%402x.png',	'RIP Pipenv: Tried Too Hard. Do what you need with pip-tools.',	'Pipenv is dead. It went all of 2019 without a single release, despite about 650 commits to master since the last release...']
#
for i in range(0, len(variable_names)):
    variable_name = variable_names[i]
    value = urllib.parse.quote(values[i])
    module_id = module_ids[i]
    if module_id:
        postEmailVariable(email_id, variable_name, value, token, base_url, module_id)
    else:
        postEmailVariable(email_id, variable_name, value, token, base_url)


html_id ="bodyText1"
type= "text"
value = '%3Cp%20style%3D%22Margin%3A0%3B-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A14px%3Bline-height%3A20px%3Bcolor%3A%23BDC1C6%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3B%22%3E%3Cp%20style%3D%27Margin%3A0%3B-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A14px%3Bline-height%3A20px%3Bcolor%3A%23BDC1C6%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3B%27%3EWelcome%20to%20our%20first%20edition%20of%20Telnyx%E2%80%99s%20Developer%20Update%21%20Here%20we%E2%80%99ll%20let%20you%20know%20about%20any%20noteworthy%20changes%20to%20our%20products%2C%20highlight%20new%20technical%20content%20and%20occasionally%20give%20you%20a%20sneak%20peek%20at%20what%20we%20have%20coming%20up.%20%3C%2Fp%3E%3C%2Fp%3E%3Cp%20style%3D%22Margin%3A0%3B-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A14px%3Bline-height%3A20px%3Bcolor%3A%23BDC1C6%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3B%22%3E%3Cbr%2F%3E%3Cbr%2F%3E%3C%2Fp%3E%3Cp%20style%3D%22Margin%3A0%3B-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A14px%3Bline-height%3A20px%3Bcolor%3A%23fff%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3Bfont-weight%3A%20bold%3B%22%3ERecent%20Releases%3C%2Fp%3E%3Cul%3E%3Cli%20style%3D%27-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A14px%3Bline-height%3A20px%3Bcolor%3A%23BDC1C6%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3BMargin-bottom%3A0px%3B%27%3ECheck%20out%20our%20suite%20of%20new%20%3Ca%20href%3D%27https%3A%2F%2Ftelnyx.com%2Frelease-notes%2Fintroducing-new-conferencing-features%27%20target%3D%27_blank%27%20id%3D%27%27%20style%3D%27color%3A%20%2300c08b%3Bfont-weight%3Abold%3B%27%3Econferencing%20features%3C%2Fa%3E%3C%2Fli%3E%20%3Cli%20style%3D%27-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A14px%3Bline-height%3A20px%3Bcolor%3A%23BDC1C6%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3BMargin-bottom%3A0px%3B%27%3ESwitch%20your%20programmable%20voice%20solution%20from%20Twilio%20in%20minutes%20with%20%3Ca%20href%3D%27https%3A%2F%2Ftelnyx.com%2Frelease-notes%2Ftexml-translator-now-available%27%20target%3D%27_blank%27%20id%3D%27%27%20style%3D%27color%3A%20%2300c08b%3Bfont-weight%3Abold%3B%27%3ETeXML%20Translator%3C%2Fa%3E%3C%2Fli%3E%20%3Cli%20style%3D%27-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A14px%3Bline-height%3A20px%3Bcolor%3A%23BDC1C6%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3BMargin-bottom%3A0px%3B%27%3EMake%20test%20calls%20directly%20from%20your%20browser%20with%20the%20%3Ca%20href%3D%27https%3A%2F%2Ftelnyx.com%2Frelease-notes%2Fnew-feature-release-portal-web-dialer%27%20target%3D%27_blank%27%20id%3D%27%27%20style%3D%27color%3A%20%2300c08b%3Bfont-weight%3Abold%3B%27%3EPortal%20Web%20Dialer%3C%2Fa%3E%3C%2Fli%3E%20%3Cli%20style%3D%27-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A14px%3Bline-height%3A20px%3Bcolor%3A%23BDC1C6%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3BMargin-bottom%3A0px%3B%27%3EGain%20insights%20on%20your%20download%20and%20upload%20usage%20with%20%3Ca%20href%3D%27https%3A%2F%2Ftelnyx.com%2Frelease-notes%2Fwireless-reporting-is-live%27%20target%3D%27_blank%27%20id%3D%27%27%20style%3D%27color%3A%20%2300c08b%3Bfont-weight%3Abold%3B%27%3EWireless%20Reports%3C%2Fa%3E%3C%2Fli%3E%20%3C%2Ful%3E'
value = re.sub('%E2%80%99', '\'', value)
print(value)
textValue= "Hello"
postEmailContent(email_id, html_id, type, value, textValue, token)