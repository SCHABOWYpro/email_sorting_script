from data_all import data_all_emails

def group_by_domain():

    domain_dic = {}

    for x in data_all_emails():
        try:
            domain_dic[x.email] = x.domain()
        except IndexError:
            continue
    group_domain_dic = {}

    for i, v in domain_dic.items():
        group_domain_dic[v] = [i] if v not in group_domain_dic.keys() else group_domain_dic[v] + [i]

    list_keys = []

    for x in group_domain_dic:
        list_keys.append(x)

    list_keys.sort()

    for x in list_keys:
        print("Domain " + x + " ("+str(len(group_domain_dic[x]))+"):")
        group_domain_dic[x].sort()
        for y in group_domain_dic[x]:
            print("     "+y)

