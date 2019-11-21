import urllib3
from bs4 import BeautifulSoup
from scrape.ScrapeObject import Scrape

from scrape.scraperMainParent import ScraperMainParent

posts = []


class Scraper(ScraperMainParent):
    def __init__(self, url_root):
        self.url_root = url_root

    def extract(self, soup, noOfAriticles):
        all_posts = self.extractParentNodes(soup,"tr","athing")
        all_sub_texts=self.extractParentNodes(soup,"td","subtext")
        all_scrapes = []
        for i in range(0, noOfAriticles):
            post = all_posts[i]
            sub = all_sub_texts[i].text.split()
            points = int(sub[0])
            author = sub[3]
            comments = int(sub[-2])
            rank = self.extractChildNode(post,"span","rank").text[:-1]
            uri = self.extractChildNode(post, "a", "storylink")["href"]
            title = self.extractChildNode(post, "a", "storylink").text
            #post_dict = {"title": title, "uri": uri, "author": author, "points": points, "comments": comments,
            #             "rank": int(rank)}
            object = Scrape(title,uri,author,points,comments,int(rank))
            strJson = object.encode_user(object)
            all_scrapes.append(strJson)
        return all_scrapes


