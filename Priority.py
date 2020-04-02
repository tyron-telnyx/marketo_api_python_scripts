from datetime import datetime

def createdAt(list, *args):

    time_list= [datetime.strptime(i, '%Y-%m-%dT%H:%M:%SZ') for i in list]
    # print(time_list)
    # print(min(time_list))
    # print(time_list.index(min(time_list)))
    return [time_list.index(min(time_list)), min(time_list).strftime('%Y-%m-%dT%H:%M:%SZ') ] #convert back to string

def leadScore(list, *args):

    new_list = list

    while 'None' in new_list:
        del new_list[new_list.index('None')]

    for i in new_list:
        if i < -10:
            return [list.index(i), i]


    return [list.index(max(new_list)), max(new_list) ]

def notNull(list,*args):

    new_list=[x.lower() for x in list]

    crap = ["empty", "unknown", "n/a", "[", "]", 'none']

    for i in new_list:
        good = "true"
        for j in crap:
            if j in i:
                good = False
        if good:
                return [new_list.index(i), list[new_list.index(i)]]

    return [0, list[0]]

priority_dict = {
            'website': [".com", ".net", ".org"],
            'country': ["United States", "USA"],
            'leadSource': ["Advertising", "Paid Search", "Organic", "Marketing Generated", "Event",  "Tradeshow",  "Content", "Webinar", "Referral", "Sales Generated","Direct"],
            'leadStatus': ['Customer','Closed Won','SQL','SDR Engaged','SAL','MQL','ReNurture','SSL','Prospects','Prospects Cold','Known','Disqualified','Not a Lead'],
            'Lead_Status__c': ['Closed Won','SQL','SDR Engaged','SAL','MQL','ReNurture','reNurture','SSL','Prospects','Prospects Cold','Known', 'Disqualified','Not a Lead'],
            'Lifecycle_Stage_Person__c': ['Closed Won','SQL','SAL','MQL','reNurture','SSL','Prospects','Prospects Cold', 'Known','Disqualified','Not a Lead'],
        }

def priority(list, line):
    for j in priority_dict[line]:
        for i in list:
            if j in i:
                return [list.index(i), i]

    return(notNull(list))

def boolTest(list, *args):
    for i in list:
        if i is True:
            return [list.index(i), i]

rules = {
            'createdAt': createdAt,
            'firstName': notNull,
            'lastName': notNull,
            'company': notNull,
            'title': notNull,
            'website': priority,
            'country': priority,
            #'mcUserId__c': [],
            'Querystring__c': notNull,
            'leadSource': priority,
            #'Lead_Source_Detail__c': [], will pull from the same lead as lead source
            'utm_source__c': notNull, #? happy with not null
            #'utm_medium__c': [], will pull from the same lead as utm_source
            #'utm_campaign__c': [], will pull from the same lead as utm_source
            'leadScore': leadScore,
            'leadStatus': priority,
            'Lead_Status__c': priority,
            'Lifecycle_Stage_Person__c': priority,
            'unsubscribed':boolTest,
            'MC_Account_Blocked__c': boolTest,
        }

def ruler (line, line_list):
    formatted_list = []
    for x in line_list:
        if x is None:
            formatted_list.append('None')
        else:
            formatted_list.append(x)
    return rules[line](formatted_list, line)