import requests


def mergeLead(base_url, token, winner_id, loser_ids, CRMmerge):

    losers_string = ','.join(loser_ids)
    url = base_url + '/rest/v1/leads/' + str(winner_id) + '/merge.json?access_token=' + token + '&leadId=&mergeInCRM=' + str(CRMmerge) + '&leadIds=' + loser_ids

    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return (response.text)