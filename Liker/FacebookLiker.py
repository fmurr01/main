from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint

#This method is responsible for automising facebook activity. It receives the driver(the webdriver that runs firefox)
#the name of the user (StringId) and the interests of the user (search terms)
def FacebookLiker(driver, StringId, searchTerms):

#Each serch term is being used in the facebook search by adding it to the URL.
#Then a variety of likebuttons are pressed. 1 of the 3 follower options and all related posts will be liked.
    for searchTerm in searchTerms:
        searchString = "https://www.facebook.com/search/top/?q=" + searchTerm
        try:
            driver.get(searchString)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        LikeButtons1 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div")
        try:
            LikeButtons1[randint(0, 2)].click()
        except Exception:
            print ("LikeButton1 could not be scrolled into view")

        driver.get("https://www.facebook.com/")
        LikeButtons2 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")
        driver.execute_script("window.scrollTo(0, 1200)")
        LikeButtons3 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")
        LikeButtons4 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div/div/div/div/div/div/div[1]/div/ul/li/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")
        LikeButtons = LikeButtons2 + LikeButtons3 + LikeButtons4
        for btn in LikeButtons:
            try:
            btn.click()
            except Exception:
                print ("Loading took too much time!")
