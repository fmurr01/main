from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint


def YoutubeLiker(driver, StringId, searchTerms, directory):

    #Loader(driver, StringId, "Youtube", directory)

    for searchTerm in searchTerms:
        searchString = "https://www.youtube.com/results?search_query=" + searchTerm
        try:
            driver.get(searchString)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        VideoButtons = driver.find_elements_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[3]/ytd-item-section-renderer/div[2]/ytd-video-renderer")
        VideoButtons[randint(0, 19)].click()
        time.sleep(30) #validate view

        LikeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]")
        DislikeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]")
        LikeButton.click()
        time.sleep(15) #validate view

    driver.back()
    #Dumper(driver, StringId, "Youtube", directory)
