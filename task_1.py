from emails import Email
from data_all import data_all_emails

def incorrect_emails():
    data = data_all_emails()
    ie_list = []
    for x in data:
        y = x.validation()
        if y == True:
            continue
        elif y == False:
            ie_list.append(x.email)

    print("Invalid emails ("+ str(len(ie_list))+ "):")

    for x in ie_list:
        print("     "+x)



