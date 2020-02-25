import re

from Marketo_API_Get_Auth import getToken
from Email.Marketo_API_Browse_Folder_For_Emails import getEmailbyBrowse
from Email.Marketo_API_Approve_Email import postApproveEmail

token = getToken()
print(token)

folder_ids = [	"2540",	"2537",	"2541",	"2542"]
email_ids = []
for id in folder_ids:
    response = getEmailbyBrowse('10', id, 'Folder', token)
    print(response.text)
    search=re.findall(r'{"id":(\d+)', response.text)
    print(search)
    email_ids.append(search)


print(email_ids)

value = '%3Cp%20style%3D%22Margin%3A0%3B-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A11px%3Bline-height%3A20px%3Bcolor%3A%235F6368%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3B%22%3E%3Ca%20target%3D%22_blank%22%20href%3D%22%7B%7Bsystem.viewAsWebpageLink%7D%7D%22%20style%3D%22-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3Bfont-size%3A11px%3Btext-decoration%3Anone%3Bcolor%3A%235F6368%3B%22%3EYou%20are%20receiving%20this%20email%20because%20you%20are%20opted%20in%20to%20%22Featured%20Content%22%3C/a%3E%3C/p%3E%3Cp%20style%3D%22Margin%3A0%3B-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-size%3A11px%3Bline-height%3A20px%3Bcolor%3A%235F6368%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3B%22%3E%3Ca%20target%3D%22_blank%22%20href%3D%22%7B%7Bsystem.viewAsWebpageLink%7D%7D%22%20style%3D%22-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3Bfont-size%3A11px%3Btext-decoration%3Anone%3Bcolor%3A%235F6368%3B%22%3EView%20in%20browser%3C/a%3E%20%7C%20%3Ca%20target%3D%22_blank%22%20style%3D%22-webkit-text-size-adjust%3Anone%3B-ms-text-size-adjust%3Anone%3Bmso-line-height-rule%3Aexactly%3Bfont-family%3Aroboto%2C%20%27helvetica%20neue%27%2C%20helvetica%2C%20arial%2C%20sans-serif%3Bfont-size%3A11px%3Btext-decoration%3Anone%3Bcolor%3A%235F6368%3B%22%20href%3D%22%7B%7Bsystem.unsubscribeLink%7D%7D%22%3EUpdate%20Email%20Preferences%3C/a%3E%3C/p%3E'
textValue = 'You%20are%20receiving%20this%20email%20because%20you%20are%20opted%20in%20to%20%22Featured%20Content%22%0A%0AView%20in%20browser%20%7C%20Update%20Email%20Preferences'

for set in email_ids:
    for id in set:
        # postEmailContent(id, "footerText2", "text", value, textValue, token)
        postApproveEmail(id, token)