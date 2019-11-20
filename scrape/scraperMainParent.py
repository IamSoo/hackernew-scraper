import urllib3
from bs4 import BeautifulSoup


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

class ScraperMainParent:
    def __init__(self):
        pass

    def scrape(self):
        req = http.request('GET', self.url_root)
        page = req.data
        soup = BeautifulSoup(page, "lxml")
        return soup

    def validateInputs(self, no_of_posts):
        if (no_of_posts <= 0):
            print(' !!! Error : Please input a postive integer.!')
            raise SystemExit
