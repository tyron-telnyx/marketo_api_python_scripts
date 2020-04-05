import requests


def mergeLead(base_url, token, winner_id, loser_ids, CRMmerge):



    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    #This code is needed because when CRM merge is true then you can only merge two leads at a time
    loser_ids = [str(x) for x in loser_ids]
    response = []
    for i in loser_ids:
        url = base_url + '/rest/v1/leads/' + str(winner_id) + '/merge.json?mergeInCRM=' + str(CRMmerge) + '&leadIds=' + i
        response.append(requests.request("POST", url, headers=headers, data=payload).text)

    return (response)