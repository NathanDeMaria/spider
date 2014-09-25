import argparse
import logging
from model import Config
from service import BaseSpider

parser = argparse.ArgumentParser()
parser.add_argument('--base_dir', help='The directory where the results file will be written')
parser.add_argument('-v', action='count', help='Increase the verbosity of log messages')
args = parser.parse_args()

config = Config()
config.verbosity = args.v
config.base_dir = args.base_dir

log = logging.getLogger("spider")
log.addHandler(logging.StreamHandler())
log.setLevel(config.verbosity)


class DemoSpider(BaseSpider):
    def __init__(self, config):
        super().__init__(config, log)

    def crawl(self, url=None):
        # do something
        data = {"interesting_data": {"oil_price": 92.04}}
        self.save(data)


spider = DemoSpider(config)
spider.crawl(url="www.bls.gov")