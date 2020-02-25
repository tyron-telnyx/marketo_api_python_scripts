from Marketo_API_Get_Auth import getToken
from Marketo_API_Clone_Smart_List import  cloneSmartList

program_ids = [	"2036",	"2047","2030",	"2055",	"2017",	"1995",	"1634",	"1676"]
#form_program_ids = [	"1417",	"1453","1681",	"1439",	"1529",	"1574",	"1634",	"1676",	"1742",	"1781",	"1840",	"1989",	"2042",	"2025",	"1596",	"2043",	"2014",	"1545",	"1455",	"1501",	"1510",	"1619",	"1632",	"1670",	"1756",	"1395"]
#program_names = [	"Content_CaseStudy_2018_04_Call Control",	"Content_CaseStudy_2018_05_PinDrop","Content_CaseStudy_2019_04_Call Tracking",	"Content_eBook_2018_05_Toll Free",	"Content_eBook_2018_07_Internationalization",	"Content_eBook_2018_11_Toot",	"Content_eBook_2019_02_Call Tracking",	"Content_eBook_2019_04_Complete Guide to SMS",	"Content_eBook_2019_06_BetterTwilioAlternative",	"Content_eBook_2019_07_ContactCenter",	"Content_eBook_2019_09_CPaaS",	"Content_eBook_2019_12_Conversational AI",	"Content_eBook_2020_01_Healthcare SMS",	"Content_eBook_2020_01_SMS Market 2020",	"Content_FactSheet_2018_12_VXC",	"Content_Guide_2020_01_MSP Get Started",	"Content_WP_2019_12_G2 Whitepaper",	"Webinar 2018_10_Tricks of the Trade",	"Webinar 2018-06_DIY_Next-Gen-Carrier",	"Webinar 2018-07_Call Control",	"Webinar 2018-08_Death to Porting",	"Webinar_2019_01_Mission Control Demo",	"Webinar_2019_02_SMS Messaging",	"Webinar_2019_04_Robocalling",	"Webinar_2019_07_Conversational AI",	"Whitepaper 2018-02_CPaaS"]

#asset_url = [	"https://go.telnyx.com/rs/028-JJW-728/images/Content_Case_Study_2019_04_Call_Tracking.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content-eBook-TollFree.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content-eBook-InternationalGuide.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content-eBook-SocialProof.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content_eBook_Call%20Tracking.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content_Ebook_2019_04_SMS_Complete_Guide_to_Messaging.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content-eBook-TheBetterTwilioAlternative.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content-eBook-ContactCenter.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content-ebook-CPaaS.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content-eBook-Conversational-ai.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content-eBook-HealthcareSMS.pdf",	"http://go.telnyx.com/rs/028-JJW-728/images/Content-ebook-StateOfSMS2020.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content_OnePager_2018_12_VXC%20AWS.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content_Guide_MSPGettingStarted.pdf",	"https://go.telnyx.com/rs/028-JJW-728/images/Content_Whitepaper_G2Comparison.pdf",	"http://go.telnyx.com/Content-Webinar-TricksOfTrade.html",	"http://go.telnyx.com/Content-Webinar-DIYNextGenCarrier.html",	"https://go.telnyx.com/Content-Webinar-CallControl.html",	"http://go.telnyx.com/Content-Webinar-DeathToPorting.html",	"https://go.telnyx.com/Content-Webinar-MissionControlDemo.html",	"http://go.telnyx.com/Content-Webinar-SMSMessaging.html",	"http://go.telnyx.com/Content-Webinar-Robocalling.html",	"http://go.telnyx.com/Content-Webinar-ConversationalAI.html",	"https://go.telnyx.com/rs/028-JJW-728/images/Content-WhitePaper-EnterpriseCPaaS.pdf"]

token = getToken()

########## Clone Email ######################
# for id, name in zip(program_ids, program_names):
#     cloneEmail("4659", "EM - " + name, id, "Program", "Created by API 2/10/2020 12pm by Tyron Pretorius", token)

######### Update Program Token ##################
# for id, url in zip(program_ids, asset_url):
#     updateProgramToken("utm", "?utm_source=mkto%26utm_medium=email%26utm_campaign=content_delivery", "text", id, "Program", token)
#     updateProgramToken("content link", url , "text", id, "Program", token)

######### Clone Smart Campaign ##################
# for id in program_ids:
#     cloneSmartCampaign ("7687", "03 Send Email", id, "Program", "Created by API 2/10/2020 16:30 by Tyron Pretorius", token)

######### Clone Smart List ##################
for id in program_ids:
    cloneSmartList ("8356398", "Bounced Emails Facebook", id, "Program", "Created by API 2/21/2020 16:00 by Tyron Pretorius", token)