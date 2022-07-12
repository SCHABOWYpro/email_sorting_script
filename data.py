import ssl
from urllib.request import urlopen
class Data:


    def __init__(self,url):

        self.url = url

    def data_list(self):
        gcontext = ssl._create_unverified_context()
        file_url = urlopen(self.url, context=gcontext).read().decode('utf-8')
        emails_list = file_url.split()
        return emails_list
