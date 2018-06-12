from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint

#This method is responsible for automising Bild activity. It receives the driver(the webdriver that runs firefox)
#the name of the user (StringId) and the interests of the user (search terms)
def BildLiker(driver, StringId, searchTerms):

#Each serch term is being used in the Bild search by adding it to the URL.
#On the result page 2 of the shown articles will be randomly read for 5 seconds.
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
            loop = True
#Sometimes the ".back"-Method does not work properly if the site has pop-ups, so it will be looped until it works.
            while loop:
                driver.back()
                time.sleep(3)
                if "suche" in driver.current_url:
                    loop = False
