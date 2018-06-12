from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint
from selenium.webdriver.common.keys import Keys

#This method is responsible for automising google activity. It receives the driver(the webdriver that runs firefox)
#the name of the user (StringId) and the interests of the user (search terms)
def GoogleLiker(driver, StringId, searchTerms):

#Each serch term is being used in google search by writing it into the search bar and pressing enter.
#On the result page 2 hits will be clicked. (Headlines prioritised)
    for searchTerm in searchTerms:
        searchBar = driver.find_element_by_xpath("//*[@id='lst-ib']")
        searchBar.clear()
        searchBar.send_keys(searchTerm)
        searchBar.send_keys(Keys.ENTER)
        time.sleep(3)

        randomNumber = random.sample(range(0, 3), 2)
        randomNumber.sort()
        for ran in randomNumber:
            News1 = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/g-section-with-header/div[2]/div/g-scrolling-carousel/div/div/div/div/g-inner-card/a/div[2]/div")
            News2 = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/h3/a")
            News = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/g-section-with-header/div[2]/div/g-inner-card/div/g-card-section/a/div/span")

            if len(News)==0:
                News = News1
            if len(News)==0:
                News = News2
            try:
                News[ran].click()
            except Exception:
                print ("GoogleLiker: Not enough interesting news")

#Sometimes the ".back"-Method does not work properly if the site has pop-ups, so it will be looped until it works.
            loop = True
            while loop:
                if "google.com" in driver.current_url:
                    loop = False
                else:
                    driver.back()
                    time.sleep(3)
