# -*- coding: utf-8 -*-
"""The purpose of this module is to implement youtubeLiker"""

import time
import random
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class googleLiker():

    def googleLiker(driver, searchTerms):

        """
        This method is responsible for automising google activity.
        Each serch term is being used in google search by writing it into the search bar and pressing enter.
        On the result page 2 hits will be clicked. (Headlines prioritised)
        several sleeps for letting the site load + it fakes realistic behaviour better

        Args:
            driver: selenium webdriver object (contains profile)
            searchTerms: string list of the profiles interests

        Raises:
            TimeoutException: if the site did not load in time
            Exception: if an element could not be found
        """

        for _searchTerm in searchTerms:
            _searchBar = driver.find_element_by_xpath("//*[@id='lst-ib']")
            _searchBar.clear()
            _searchBar.send_keys(_searchTerm)
            _searchBar.send_keys(Keys.ENTER)
            time.sleep(5)

            """
            _news1 are slim Headlines, _news2 are normal results and News are rectangle headlines. Priority: _news>_news1>_news2
            _news are searched for twice: Once for their numbers and in the second call to click them. This has to be done again,
            because Selenium will identify them as different elements after the driver.back call
            """

            _news1 = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/g-section-with-header/div[2]/div/g-scrolling-carousel/div/div/div/div/g-inner-card/a/div[2]/div")
            _news2 = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/h3/a")
            _news = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/g-section-with-header/div[2]/div/g-inner-card/div/g-card-section/a/div/span")
            if len(_news)<=1:
                _news = _news1
            if len(_news)==0:
                _news = _news2

            _randomNumber = random.sample(range(0, (len(_news))), 2)
            _randomNumber.sort()
            for _ran in _randomNumber:
                _news1 = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/g-section-with-header/div[2]/div/g-scrolling-carousel/div/div/div/div/g-inner-card/a/div[2]/div")
                _news2 = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/h3/a")
                _news = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/g-section-with-header/div[2]/div/g-inner-card/div/g-card-section/a/div/span")
                if len(_news)==0:
                    _news = _news1
                if len(_news)==0:
                    _news = _news2
                try:
                    _news[_ran].click()
                except Exception:
                    print ("GoogleLiker: Not enough interesting news")
                time.sleep(5)
                #Sometimes the ".back"-Method does not work properly if the site has pop-ups, so it will be looped until it works.
                _loop = True
                while _loop:
                    try:
                        driver.back()
                    except TimeoutException:
                        print ("Loading took too much time!")
                    time.sleep(3)
                    if "google.com" in driver.current_url:
                        _loop = False
