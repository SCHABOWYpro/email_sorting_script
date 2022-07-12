import re

class Email:

    def __init__(self, email):


        self.email = email

    def domain(self):

        domain_from_email = self.email
        email_to_split = domain_from_email.split("@")
        email_domain = email_to_split[1]
        return email_domain

    def validation(self):

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if re.search(regex, self.email):
            return True
        else:
            return False