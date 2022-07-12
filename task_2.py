from data_all import data_all_emails

def search_str(s):

    search_email_list = []

    for x in data_all_emails():
        if s in x.email and x.validation():
            search_email_list.append(x.email)

    sel_set = set(search_email_list)

    print("Found emails with "+ "'"+s+"' in email ("+str(len(sel_set))+ "):")

    for y in sel_set:
        print("     "+y)

