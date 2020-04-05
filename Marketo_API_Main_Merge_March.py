import pandas as pd
import json

from Priority import ruler
from AppendDict import appendDict
from Marketo_API_Get_Auth import getToken
from Marketo_API_Query_Lead import getLead
from Marketo_API_Merge import mergeLead
from Marketo_API_Create_Update_Lead import createUpdateLead

base_url = "https://028-jjw-728.mktorest.com"
field_names = 'id,email,createdAt,firstName,lastName,company,title,website,country,mcUserId__c,Querystring__c,leadSource,Lead_Source_Detail__c,utm_source__c,utm_medium__c,utm_campaign__c,leadScore,leadStatus,Lead_Status__c,Lifecycle_Stage_Person__c,unsubscribed,MC_Account_Blocked__c'

raw_list = pd.read_csv('/home/localadmin/Downloads/Rules for Merging Leads  - Export.csv')
ids = raw_list['Id'].tolist()
ids = [str(i) for i in ids]
emails = raw_list['Email Address'].tolist() # *********** Assume the Email Address List is sorted ********************
# print (ids)
# print (emails)

mc_user_id_conflicts =[]
get_lead_errors = []
merge_errors = []

field_dict = {
    'id': [], 'email': [], 'createdAt': [], 'firstName': [], 'lastName': [], 'company': [], 'title': [], 'website': [],
    'country': [], 'mcUserId__c': [], 'Querystring__c': [], 'leadSource': [], 'Lead_Source_Detail__c': [],
    'utm_source__c': [], 'utm_medium__c': [], 'utm_campaign__c': [], 'leadScore': [], 'leadStatus': [],
    'Lead_Status__c': [], 'Lifecycle_Stage_Person__c': [], 'unsubscribed': [], 'MC_Account_Blocked__c': []
}

final_dict = {
    'id': [], 'email': [], 'createdAt': [], 'firstName': [], 'lastName': [], 'company': [], 'title': [], 'website': [],
    'country': [], 'mcUserId__c': [], 'Querystring__c': [], 'leadSource': [], 'Lead_Source_Detail__c': [],
    'utm_source__c': [], 'utm_medium__c': [], 'utm_campaign__c': [], 'leadScore': [], 'leadStatus': [],
    'Lead_Status__c': [], 'Lifecycle_Stage_Person__c': [], 'unsubscribed': [], 'MC_Account_Blocked__c': []
}

i = 4157
#all_loser_ids = []
total_count = 0
count = 0
update_leads = ['']
while i < 4700:
    total_count = total_count + count
    count = 0
    token = getToken()
    print(token)

    while count < 100 : #len(ids):

        stop = False
        field_dict = field_dict.fromkeys(field_dict, [])
        final_dict = final_dict.fromkeys(final_dict, [])

        try:
            id1 = json.loads(getLead(base_url, token, ids[i], field_names))["result"][0]
            appendDict(field_dict, id1)
        except:
            stop = True

        j=i+1
        while (emails[i] == emails [j]):
            try:
                idj = json.loads(getLead(base_url, token , ids[j], field_names))["result"][0]
                appendDict(field_dict, idj)
            except:
                stop = True

            # print(idj)
            j=j+1

        i = j

        if stop:
            stop=False
            get_lead_errors.append(field_dict['id'])
            continue

        else:
            for line in field_dict:
                if all(elem==field_dict[line][0] for elem in field_dict[line]) and line != 'createdAt':
                    final_dict[line] =field_dict[line][0]
                else:
                    if line in ['email', 'id', 'Lead_Source_Detail__c', 'utm_source__c', 'utm_medium__c' ,'utm_campaign__c' ]:
                        pass
                    elif line =="createdAt":
                        [index, value] = ruler(line, field_dict[line])
                        final_dict[line] = value
                        final_dict['id'] = field_dict['id'][index]
                    elif line == "mcUserId__c":
                        new_list = field_dict[line]

                        while None in new_list:
                           del new_list[new_list.index(None)]

                        if all(elem==new_list[0] for elem in new_list):
                            final_dict[line] = field_dict[line][field_dict[line].index(new_list[0])]
                        else:
                            with open('/home/localadmin/Downloads/mc_conflicts.csv', 'a') as fd:
                                fd.write(str(str(final_dict['mcUserId__c']) + str(field_dict['mcUserId__c'])))
                            mc_user_id_conflicts.append(field_dict[line])
                            # errors.append(field_dict['id'])
                            continue #do not merge if their mc user ids are different
                    elif line == 'leadSource':
                        [index, value]=ruler(line, field_dict[line])
                        final_dict[line] = value
                        final_dict["Lead_Source_Detail__c"] = field_dict["Lead_Source_Detail__c"][index]
                        if field_dict["utm_source__c"][index]: #not empty
                            final_dict["utm_source__c"] = field_dict["utm_source__c"][index]
                            final_dict["utm_medium__c"] = field_dict["utm_medium__c"][index]
                            final_dict["utm_campaign__c"] = field_dict["utm_campaign__c"][index]
                        else: #if empty then get the 3xutm parameters from another lead
                            [index, value] = ruler("utm_source__c", field_dict["utm_source__c"])

                            final_dict["utm_campaign__c"] = field_dict["utm_campaign__c"][index]
                            final_dict["utm_medium__c"] = field_dict["utm_medium__c"][index]
                            final_dict["utm_campaign__c"] = field_dict["utm_campaign__c"][index]
                    else:
                        final_dict[line] = ruler(line, field_dict[line])[1]

            print(count)
            print(i)
            print(total_count)
            print(field_dict)
            print(final_dict)
            print('')

            loser_ids = field_dict['id']
            loser_ids.remove(final_dict['id'])

            #all_loser_ids.append(loser_ids)
            update_leads[0] = final_dict
            response = mergeLead(base_url, token, final_dict['id'], loser_ids, True)
            print(response)
            if '"success":false' in str(response):
                with open('/home/localadmin/Downloads/merge_errors.csv', 'a') as fd:
                    fd.write(str(str(final_dict['id'])+str(field_dict['id'])))
            else:
                response = createUpdateLead(base_url, token, update_leads)
                print(response)
                if '"success":false' in str(response):
                    with open('/home/localadmin/Downloads/update_errors.csv', 'a') as fd:
                        fd.write(str(str(final_dict['id']) + str(field_dict['id'])))


            count=count+1

