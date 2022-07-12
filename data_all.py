from data import Data
from emails import Email


def data_all_emails():
    data_set_1 = Data("https://git.profil-software.com/recruitment-05-2022/recruitment-task-backend-internship/-/raw/main/emails/email-pack-1.txt").data_list()
    data_set_2 = Data("https://git.profil-software.com/recruitment-05-2022/recruitment-task-backend-internship/-/raw/main/emails/emails-pack-2.txt").data_list()
    data_set_3 = Data("https://git.profil-software.com/recruitment-05-2022/recruitment-task-backend-internship/-/raw/main/emails/emails3.txt").data_list()
    data_set_4 = Data("https://git.profil-software.com/recruitment-05-2022/recruitment-task-backend-internship/-/raw/main/emails/other-emails4.txt").data_list()
    data_set_csv_raw = Data("https://git.profil-software.com/recruitment-05-2022/recruitment-task-backend-internship/-/raw/main/emails/last-email-pack.csv").data_list()
    data_set_csv = []

    for x in data_set_csv_raw:
        y = x.split(";")
        data_set_csv.append(y[1])
    data_set_csv.pop(0)

    all_emails = []

    for x in data_set_1+data_set_2+data_set_3+data_set_4+data_set_csv:
        user = Email(x)
        all_emails.append(user)
    return all_emails

