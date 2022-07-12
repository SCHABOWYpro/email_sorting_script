from task_1 import incorrect_emails
from task_2 import search_str
from task_3 import group_by_domain
from task_4 import find_emails_not_in_logs
def main():



    while True:
        print("""
            ====== Email sorting script =======
            For list of incorrect emails type:
            --incorrect-emails  or   -ic
            For list of grouped emails by domain type:
            --group-by-domanin  or   -gbd
            If you want to search email by given word type:
            --serach or  -s 
            For emails not in logs type:
            --find-emails-not-in-logs or -feil

            Type stop to quit
            ======= Type your command below ========
            """)

        x = str(input())
        if x == "--incorrect-emails" or x == "-ic":
            incorrect_emails()
            continue
        elif x == "--group-by-domain" or x == "-gbd":
            group_by_domain()
            continue
        elif x == "--search" or x== "-s":
            print("What word do you search for?")
            while True:
                try:
                    x = str(input())
                    search_str(x)
                    break
                except ValueError:
                    print("This word is invalid, please try again")
                    continue
        elif x == "--find-emails-not-in-logs" or x == "-feil":
            print("Add logfile URL")
            while True:
                try:
                    x = str(input())
                    find_emails_not_in_logs(x)
                    break
                except ValueError:
                    print("This URL is invalid")
                    continue

        elif x == "stop":
            break



    #incorrect_emails()
    #search_str("agustin")
    #roup_by_domain()
    #find_emails_not_in_logs("https://git.profil-software.com/recruitment-05-2022/recruitment-task-backend-internship/-/raw/main/email-sent.logs")


if __name__=="__main__":
    main()