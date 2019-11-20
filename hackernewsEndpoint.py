from flask import Flask,request,Response
from flask import jsonify
import argparse
import yaml
from scrape.scraperMain import Scraper

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def status():
    app.logger.info("testing warning log")
    return 'I am running!!'

@app.route("/hackernews")
def runScraper():
    noOfPosts = request.args["posts"]
    app.logger.info("testing warning log")
    if(int(noOfPosts) <= 0):
        return "Please input a positive integer for the no of posts you want see."
    return jsonify(callScraperClass(int(noOfPosts)))

def callScraperClass(no_of_posts):
    with open('config.yml') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    ROOT_URL = cfg['ROOT_URL']
    scraper = Scraper(ROOT_URL)
    scraper.validateInputs(no_of_posts)
    soup = scraper.scrape()
    post_dict_list = scraper.extract(soup, no_of_posts)
    app.logger.info("post_dict_list {}",post_dict_list)
    return post_dict_list


if __name__=='__main__':
    app.run(debug=False, host='0.0.0.0')