import urllib3
from bs4 import BeautifulSoup

from scrape.scraperMainParent import ScraperMainParent

posts = []


class Scraper(ScraperMainParent):
    def __init__(self, url_root):
        self.url_root = url_root

    def extract(self, soup, noOfAriticles):
        all_posts = soup.find_all("tr", {"class": "athing"})
        all_sub_texts = soup.find_all("td", {"class": "subtext"})
        all_scrapes = []
        for i in range(0, noOfAriticles):
            post = all_posts[i]
            sub = all_sub_texts[i].text.split()
            points = int(sub[0])
            author = sub[3]
            comments = int(sub[-2])

            rank = int(post.find("span", {"class": "rank"}).text[:-1])
            uri = post.find("a", {"class": "storylink"})["href"]
            title = post.find("a", {"class": "storylink"}).text
            post_dict = {}
            post_dict = {"title": title, "uri": uri, "author": author, "points": points, "comments": comments,
                         "rank": rank}
            all_scrapes.append(post_dict)
        return all_scrapes


