# -*- coding: utf-8 -*-
"""The purpose of this module is to implement redditLiker"""

import time
import random
from random import randint
from selenium.common.exceptions import TimeoutException

class redditLiker():

    def redditLiker(driver, searchTerms):

        """
        This method is responsible for automising reddit activity.
        Each serch term is being used in the reddit search by adding it to the URL.
        Then 2 of the 3 shown subscribe options will be clicked and 1/3 of all shown inserations liked.
        There are a bunch of sleeps, because even though ".get" waits for the entire page to load,
        sometimes the buttons load a little bit later. Also it fakes real behaviour better.

        Args:
            driver: selenium webdriver object (contains profile)
            searchTerms: string list of the profiles interests

        Raises:
            TimeoutException: if the site did not load in time
            Exception: if an element/button could not be found
        """

        for _searchTerm in searchTerms:
            _searchString = "https://new.reddit.com/search?q=" + _searchTerm + "&t=all&sort=new"
            try:
                driver.get(_searchString)
                time.sleep(2)
                print ("Page is ready!")
            except TimeoutException:
                print ("Loading took too much time!")

            _subscribeButtons = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/a/div[3]/button")
            print(len(_subscribeButtons))
            _randomNumber = random.sample(range(0, 3), 2)
            _randomNumber.sort()
            for _ran in _randomNumber:
                try:
                    _subscribeButtons[_ran].click()
                    time.sleep(1)
                except Exception:
                    print ("SubscribeButtons could not be scrolled into view")
            
             _likeButtons = driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/div/div/div/div[1]/div/button[1]')
             _lmt = len(_likeButtons)
             _smallLmt = int(_lmt/3)
             _randomNumber = random.sample(range(0, _lmt), _smallLmt)
             _randomNumber.sort()
             for i in range (0, _smallLmt):
                 try:
                     _likeButtons[_randomNumber[i]].click()
                 except Exception:
                     print ("Like could not be scrolled into view")
