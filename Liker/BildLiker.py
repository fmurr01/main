from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint


def BildLiker(driver, StringId, searchTerms, directory):

    for searchTerm in searchTerms:
        searchString = "https://www.bild.de/suche.bild.html?query=" + searchTerm
        try:
            driver.get(searchString)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        randomNumber = random.sample(range(0, 9), 2)
        randomNumber.sort()
        for ran in randomNumber:
            News = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[5]/div/section/ol/li/div/a/img")
            News[ran].click()
            time.sleep(3)
            driver.back()
