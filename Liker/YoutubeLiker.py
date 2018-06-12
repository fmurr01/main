from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint

#This method is responsible for automising reddit activity. It receives the driver(the webdriver that runs firefox)
#the name of the user (StringId) and the interests of the user (search terms)
def YoutubeLiker(driver, StringId, searchTerms):

#Each serch term is being used in the youtube search by adding it to the URL.
#On the results page 1 video will be randomly viewed for 45 seconds to assure it being registered as a view.
#The video will be liked after 30 seconds
    for searchTerm in searchTerms:
        searchString = "https://www.youtube.com/results?search_query=" + searchTerm
        try:
            driver.get(searchString)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        VideoButtons = driver.find_elements_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[3]/ytd-item-section-renderer/div[2]/ytd-video-renderer")
        try:
            VideoButtons[randint(0, len(VideoButtons)-1)].click()
            print ("Page is ready!")
        except Exception:
            print ("Loading took too much time!")

        time.sleep(30) #validate view
        try:
            LikeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]")
            #DislikeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]")
            LikeButton.click()
        except Exception:
            print ("Loading took too much time!")
        time.sleep(15) #validate view

#Sometimes the ".back"-Method does not work properly if the site has pop-ups, so it will be looped until it works.
    loop = True
    while loop:
        driver.back()
        time.sleep(5)
        if "results?search" in driver.current_url:
            loop = False
