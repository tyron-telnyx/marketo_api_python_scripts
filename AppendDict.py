def appendDict (dict_master, lead_dict):

    for line in lead_dict:
        dict_master[line] = dict_master[line]+[lead_dict[line]]

    return dict_master
