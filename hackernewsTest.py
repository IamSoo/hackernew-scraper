import unittest
from scrape.scraperMain import Scraper
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


class HackernewsTest(unittest.TestCase):
    def testExtractChildNode(self):
        soup = BeautifulSoup('<html><td align="right" class="title" valign="top"><span class="rank">28</span></td></html>','lxml')
        scraper = Scraper("")
        result = scraper.extractChildNode(soup,"span","rank")
        self.assertEqual('28',result.text)

    def testExtract(self):
        soup = BeautifulSoup('<tr class="athing" id="21593806"><td align="right" class="title" valign="top"><span class="rank">1.</span></td> <td class="votelinks" valign="top"><center><a href="vote?id=21593806&amp;how=up&amp;goto=news" \
        id="up_21593806"><div class="votearrow" title="upvote"></div></a></center></td><td class="title"><a class="storylink"\
        href="https://www.economist.com/books-and-arts/2019/11/14/a-kurt-vonnegut-museum-opens-in-indianapolis">Kurt Vonnegut Museum Opens in Indianapolis</a>\
        <span class="sitebit comhead"> (<a href="from?site=economist.com"><span class="sitestr">economist.com</span></a>)</span></td></tr><tr><td colspan="2"></td><td class="subtext"><span class="score" id="score_21593806">51 points</span> by <a class="hnuser" href="user?id=pseudolus">pseudolus</a> <span class="age">\
        <a href="item?id=21593806">1 hour ago</a></span> <span id="unv_21593806"></span> | <a href="hide?id=21593806&amp;goto=news">hide</a> | <a href="item?id=21593806">12 comments</a> </td></tr>','lxml')
        scraper = Scraper("")
        result = scraper.extract(soup, 1)
        self.assertEqual('pseudolus', result[0].get("author"))
        self.assertEqual(12, result[0].get("comments"))
        self.assertEqual(1, result[0].get("rank"))


if __name__ == '__main__':
    unittest.main()