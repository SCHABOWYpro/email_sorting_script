from data_all import data_all_emails
from data import Data

def find_emails_not_in_logs(path):

    logs_raw = Data(path).data_list()

    logs_raw.insert(0,0)
    logs = logs_raw[::8]
    logs.pop(0)

    not_send_emails = []

    for x in data_all_emails():
        y = "'"+x.email+"'"
        if y not in logs and x.validation():
            not_send_emails.append(x.email)

    not_send_emails.sort()

    print("Emails not sent " + "(" + str(len(not_send_emails))+"):")
    for x in not_send_emails:
       print(x)

