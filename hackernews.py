import argparse
import yaml
from scrape.scraperMain import Scraper

if __name__ == "__main__":
    # Load Configs
    with open('config.yml') as ymlfile:
        cfg = yaml.load(ymlfile,Loader=yaml.FullLoader)

    ROOT_URL = cfg['ROOT_URL']

    parser = argparse.ArgumentParser(description="Input arguments")
    parser.add_argument('--posts',required=True,type=int, help='How many posts to print,a positive integer')
    
    args = parser.parse_args()
    no_of_posts = args.posts

    scraper = Scraper(ROOT_URL)
    scraper.validateInputs(no_of_posts)
    soup = scraper.scrape()
    post_dict_list = scraper.extract(soup,no_of_posts)
    print(post_dict_list)
