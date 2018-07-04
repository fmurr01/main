# -*- coding: utf-8 -*-
"""The purpose of this module is to implement redditLiker"""

import time
import random
from random import randint
from selenium.common.exceptions import TimeoutException

class facebookLiker():

    def facebookLiker(driver, searchTerms):

        """
        This method is responsible for automising facebook activity.
        Each serch term is being used in the facebook search by adding it to the URL.
        Then a variety of likebuttons are pressed. 1 of the 3 follower options and all related posts will be liked.

        Args:
            driver: selenium webdriver object (contains profile)
            searchTerms: string list of the profiles interests

        Raises:
            TimeoutException: if the site did not load in time
            Exception: if an element could not be found
        """

        for _searchTerm in searchTerms:
            _searchString = "https://www.facebook.com/search/top/?q=" + _searchTerm
            try:
                driver.get(_searchString)
                print ("Page is ready!")
            except TimeoutException:
                print ("Loading took too much time!")

            _likeButtons1 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div")
            try:
                _likeButtons1[randint(0, 2)].click()
            except Exception:
                print ("LikeButton1 could not be scrolled into view")

            driver.get("https://www.facebook.com/")
            _likeButtons2 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")
            driver.execute_script("window.scrollTo(0, 1200)")
            _likeButtons3 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")
            _likeButtons4 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div/div/div/div/div/div/div[1]/div/ul/li/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")
            _likeButtons = _likeButtons2 + _likeButtons3 + _likeButtons4
            for _btn in _likeButtons:
                try:
                    _btn.click()
                except Exception:
                    print ("Button could not be found")
