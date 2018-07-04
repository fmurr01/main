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
        config = SafeConfigParser()
        config.read('config.ini')
        user = config.get('user', 'used').split()
        columns = config.get('pages', 'scraped').split()
        ProfileDirectory = config.get('directories', 'profiledirectory')

        #This datalist will contain datalists aka arrays
        metaDatalist = []

        #for every user a webdriver will be started with the set Firefox profile and proxy from the config
        for usr in user:
            print(usr)
            tmpProfile = webdriver.FirefoxProfile(ProfileDirectory + config.get('profiles', usr))
            driver = webdriver.Firefox(firefox_profile=tmpProfile, capabilities=Proxy(config.get('proxy', usr)))

            #this datalist will contain the scraped prices of one user for each website as an array.
            datalist = []
            for col in columns:
                #each col aka website URL will be called
                driver.get(col)
                time.sleep(3)

                #BeautifulSoup will scrape the Html source page and filter for set words individually for each site
                soup=BeautifulSoup(driver.page_source, "html.parser")
                price_box = soup.find('span', attrs={'data-reactid':'76'}) #Esprit
                #price_box = soup.find('span', attrs={'class':'price'}) #H&M, has severe bot protection
                #price_box = soup.find('h4', attrs={'class':'h-text h-color-red title-3 h-p-top-m'}) #zalando
                #price_box = soup.find('div', attrs={'class':'price orange'}) #cyberport
                #price_box = soup.find('text', attrs={'class':'nbb-svg-outline'}) #notebooksbilliger, has bot protection
                #price_box = soup.find('div', attrs={'itemprop':'price'}) #conrad, has bot protection
                #price_box = soup.find('span', attrs={'itemprop':'price'}) #tchibo
                #price_box = soup.find('div', attrs={'class':'price'}) #mediamarkt
                #price_box = soup.find('span', attrs={'id':'normalPriceAmount'}) #otto
                print(price_box.prettify())
                #Get only the price from the html line that contains it
                price = "N/A"
                try:
                    price = price_box.text
                except Exception:
                    print ("No price found")

                datalist.append(price)

            metaDatalist.append(datalist)
            driver.quit()

        #Build a DataFrame and save it using Pandas
        df = pd.DataFrame(metaDatalist, columns=columns)
        df.to_csv('priceDataFrame.csv', sep='\t', encoding='utf-8')
        print(df)
