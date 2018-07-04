# -*- coding: utf-8 -*-
"""The purpose of this module is to implement redditLiker"""

import time
import random
from random import randint
from selenium.common.exceptions import TimeoutException

class bildLiker():

    def bildLiker(driver, searchTerms):

        """
        This method is responsible for automising Bild activity.
        Each serch term is being used in the Bild search by adding it to the URL.
        On the result page 2 of the shown articles will be randomly read for 5 seconds.

        Args:
            driver: selenium webdriver object (contains profile)
            searchTerms: string list of the profiles interests

        Raises:
            TimeoutException: if the site did not load in time
        """

        for _searchTerm in searchTerms:
            _searchString = "https://www.bild.de/suche.bild.html?query=" + _searchTerm
            try:
                driver.get(_searchString)
                print ("Page is ready!")
            except TimeoutException:
                print ("Loading took too much time!")

            _randomNumber = random.sample(range(0, 9), 2)
            _randomNumber.sort()
            for _ran in _randomNumber:
                _news = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[5]/div/section/ol/li/div/a/img")
                _news[_ran].click()
                time.sleep(3)
                _loop = True
    #Sometimes the ".back"-Method does not work properly if the site has pop-ups, so it will be looped until it works.
                while _loop:
                    driver.back()
                    time.sleep(3)
                    if ".de/suche" in driver.current_url:
                        _loop = False
