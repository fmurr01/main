# -*- coding: utf-8 -*-
"""The purpose of this module is to implement youtubeLiker"""

import time
import random
from random import randint
from selenium.common.exceptions import TimeoutException

class youtubeLiker():

    def youtubeLiker(driver, searchTerms):

        """
        This method is responsible for automising youtube activity.
        Each serch term is being used in the youtube search by adding it to the URL.
        On the results page 1 video will be randomly viewed for 45 seconds to assure it being registered as a view.
        The video will be liked after 30 seconds

        Args:
            driver: selenium webdriver object (contains profile)
            searchTerms: string list of the profiles interests

        Raises:
            TimeoutException: if the site did not load in time
            Exception: if an element could not be found
        """

        for _searchTerm in searchTerms:
            _searchString = "https://www.youtube.com/results?search_query=" + _searchTerm
            try:
                driver.get(_searchString)
                print ("Page is ready!")
            except TimeoutException:
                print ("Loading took too much time!")

            _videoButtons = driver.find_elements_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[3]/ytd-item-section-renderer/div[2]/ytd-video-renderer")
            try:
                _videoButtons[randint(0, len(_videoButtons)-1)].click()
                print ("Page is ready!")
            except Exception:
                print ("Loading took too much time!")

            time.sleep(30) #validate view
            try:
                _likeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]")
                #_dislikeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]")
                _likeButton.click()
            except Exception:
                print ("Could not find/click button")
            time.sleep(15) #validate view

    #Sometimes the ".back"-Method does not work properly if the site has pop-ups, so it will be looped until it works.
        loop = True
        while loop:
            driver.back()
            time.sleep(5)
            if "results?search" in driver.current_url:
                loop = False
