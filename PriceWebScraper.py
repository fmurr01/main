# -*- coding: utf-8 -*-
"""The purpose of this module is solely to implement priceWebScraper"""

import time
import re
from configparser import SafeConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
from support import *

class priceWebScraper():


    def scrapePrices():

        """
        Consists of two loops:
        -The outer loop uses the profile names, locations and proxy-data of the firefox profiles to create
        a selenium driver for each user.
        -The inner loop will visit shoppin-urls as specified in the config, uses BeautifulSoup to scrape
        the sites context, filters for the price and uses Pandas to build a .csv containing a DataFrame
        of prices in relation to the url to analyse it later.

        Returns: priceDataFrame.csv
        """
        #load config
        _config = SafeConfigParser()
        _config.read('config.ini')
        _user = _config.get('scrapeUser', 'used').split()
        _columns = _config.get('pages', 'scraped').split()
        _profileDirectory = _config.get('directories', 'profileDirectory')

        #This datalist will contain datalists aka arrays
        _metaDatalist = []

        #for every user a webdriver will be started with the set Firefox profile and proxy from the config
        for _usr in _user:
            print(_usr)
            _tmpProfile = webdriver.FirefoxProfile(_profileDirectory + _config.get('profiles', _usr))
            _driver = webdriver.Firefox(firefox_profile=_tmpProfile, capabilities=support.proxy(_config.get('proxy', _usr)))

            #this datalist will contain the scraped prices of one user for each website as an array.
            _datalist = []
            for _col in _columns:
                #each col aka website URL will be called
                _driver.get(_col)
                time.sleep(2)

                #BeautifulSoup will scrape the Html source page and filter for set words individually for each site
                _soup=BeautifulSoup(_driver.page_source, "html.parser")


                _priceBox = _soup.find('span', attrs={'class':'spv-price__selling'}) #Esprit

                #_priceBox = soup.find('span', attrs={'class':'price'}) #H&M, has severe bot protection
                #_priceBox = soup.find('h4', attrs={'class':'h-text h-color-red title-3 h-p-top-m'}) #zalando
                #_priceBox = soup.find('div', attrs={'class':'price orange'}) #cyberport
                #_priceBox = soup.find('text', attrs={'class':'nbb-svg-outline'}) #notebooksbilliger, has bot protection
                #_priceBox = soup.find('div', attrs={'itemprop':'price'}) #conrad, has bot protection
                #_priceBox = soup.find('span', attrs={'itemprop':'price'}) #tchibo
                #_priceBox = soup.find('div', attrs={'class':'price'}) #mediamarkt
                #_priceBox = soup.find('span', attrs={'id':'normalPriceAmount'}) #otto
                #Get only the price from the html line that contains it
                _price = "00,00"
                try:

                    _price = _priceBox.text
                    _middle = _price.find(",")
                    _price = _price[_middle-2:_middle+3]
                except Exception:
                    print ("No price found")


                _datalist.append(_price)

            _metaDatalist.append(_datalist)
            #_driver.quit()

        #Build a DataFrame and save it using Pandas
        _df = pd.DataFrame(_metaDatalist, columns=_columns)
        _df.to_csv('priceDataFrame.csv', sep='\t', encoding='utf-8')
        print(_df)

    scrapePrices()
