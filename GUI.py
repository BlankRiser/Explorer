import argparse
import time
import json

from gooey import Gooey
from functools import reduce

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

from amazonTracker import AmazonAPI
from pdfreport import GeneratepdfReport
from jsonReport import GeneratejsonReport


@Gooey
def main():
    parser = argparse.ArgumentParser(description='Do stuff with numbers.')
    parser.add_argument(
        '-a', '--name', help='Enter the name of the product', required=True, nargs='+')
    parser.add_argument(
        '-m', '--minprice', help='Minimum Price you can pay', required=True, nargs='+')
    parser.add_argument(
        '--maxprice', help='Maximum Price you can pay', required=True, nargs='+')

    args = vars(parser.parse_args())

    NAME = args['name'][0]
    CURRENCY = '₹'
    MIN_PRICE = int(args['minprice'][0])
    MAX_PRICE = int(args['maxprice'][0])
    FILTERS = {
        'min': MIN_PRICE,
        'max': MAX_PRICE
    }
    BASE_URL = "http://www.amazon.in/"

    amazondata = AmazonAPI(NAME, FILTERS, BASE_URL, CURRENCY)
    data = amazondata.run()
    GeneratejsonReport(NAME, FILTERS, BASE_URL, CURRENCY, data)
    GeneratepdfReport(data)


main()
