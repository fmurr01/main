# -*- coding: utf-8 -*-
"""The purpose of this module is to implement twitterLiker"""

import time
import random
from random import randint
from selenium.common.exceptions import TimeoutException

class twitterLiker():

    def twitterLiker(driver, searchTerms):

        """
        This method is responsible for automising twitter activity.
        Each serch term is being used in the twitter search by adding it to the URL.
        On that page the shown users will receive a follow by finding the element by XPATH and clicking it.
        To get newer tweets it directs to the "new" page and randomly like 3 shown tweets.

        Args:
            driver: selenium webdriver object (contains profile)
            searchTerms: string list of the profiles interests

        Raises:
            TimeoutException: if the site did not load in time
            Exception: if an element(heart/follow) could not be found
        """

        for _searchTerm in searchTerms:
            _searchString = "https://twitter.com/search?q=" + _searchTerm + "&src=typd"
            try:
                driver.get(_searchString)
                time.sleep(1)
                print("Page is ready!")
            except TimeoutException:
                print ("Loading took too much time!")

            _followButtons = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/ol[1]/li[1]/div[2]/div/div/div/div/div[1]/div/div/div/span[2]")

            print(len(_followButtons))
            for _btn in _followButtons:
                try:
                    _btn.click()
                except Exception:
                    print ("Already Followed/Follow could not be scrolled into view")

            _searchString2 = "https://twitter.com/search?f=tweets&vertical=news&q=" + _searchTerm + "&src=typd"
            try:
                driver.get(_searchString2)
                time.sleep(1)
                print ("Page is ready!")
            except TimeoutException:
                print ("Loading took too much time!")
            _heartButtons = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/ol[1]/li/div/div[2]/div/div[2]/div[3]/button[1]")
            _randomNumber = random.sample(range(0, 9), 3)
            _randomNumber.sort()
            for i in range (0, 3):
                try:
                    _heartButtons[_randomNumber[i]].click()
                except Exception:
                    print ("Heart could not be scrolled into view")
