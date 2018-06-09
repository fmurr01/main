from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint


def FacebookLiker(driver, StringId, searchTerms, directory):

    #Loader(driver, StringId, "Facebook", directory)

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
        #
        # PageLikeButtons = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[3]/div[1]/div[2]/span[1]/span[1]')
        # print(len(PageLikeButtons))
        # try:
        #     PageLikeButtons[randint(0, 2)].click()
        # except Exception:
        #     print ("PageLikeButtons could not be scrolled into view")

        driver.get("https://www.facebook.com/")
        LikeButtons2 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")
        driver.execute_script("window.scrollTo(0, 1200)")
        LikeButtons3 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")
        LikeButtons4 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div/div/div/div/div/div/div[1]/div/ul/li/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")



        LikeButtons = LikeButtons2 + LikeButtons3 + LikeButtons4

        print(len(LikeButtons), len(LikeButtons2), len(LikeButtons3))
        for btn in LikeButtons2:
        #    try:
            btn.click()
        #    except Exception:
        #        print ("LikeButtons2 could not be scrolled into view")

    #Dumper(driver, StringId, "Facebook", directory)
