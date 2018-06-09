from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint
from selenium.webdriver.common.keys import Keys

def GoogleLiker(driver, StringId, searchTerms, directory):

    for searchTerm in searchTerms:
        searchBar = driver.find_element_by_xpath("//*[@id='lst-ib']")
        searchBar.clear()
        searchBar.send_keys(searchTerm)
        searchBar.send_keys(Keys.ENTER)
        time.sleep(3)

        randomNumber = random.sample(range(0, 3), 2)
        randomNumber.sort()
        for ran in randomNumber:
            News1 = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/g-section-with-header/div[2]/div/g-scrolling-carousel/div/div/div/div/g-inner-card/a/div[2]/div")
            News2 = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/h3/a")
            News = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/g-section-with-header/div[2]/div/g-inner-card/div/g-card-section/a/div/span")
            if len(News)==0:
                News = News1
            if len(News)==0:
                News = News2
            try:
                News[ran].click()
            except Exception:
                print ("GoogleLiker: Not enough interesting news")

            loop = True
            while loop:
                driver.back()
                time.sleep(3)
                if "google.com" in driver.current_url:
                    loop = False
