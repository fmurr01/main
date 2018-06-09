from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint

def TwitterLiker(driver, StringId, searchTerms, directory):

    for searchTerm in searchTerms:
        searchString = "https://twitter.com/search?q=" + searchTerm + "&src=typd"
        try:
            driver.get(searchString)
            time.sleep(1)
            print("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        FollowButtons = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/ol[1]/li[1]/div[2]/div/div/div/div/div[1]/div/div/div/span[2]/button[1]")
        for btn in FollowButtons:
            try:
                btn.click()
            except Exception:
                print ("Follow could not be scrolled into view")

        searchString2 = "https://twitter.com/search?f=tweets&vertical=news&q=" + searchTerm + "&src=typd"
        try:
            driver.get(searchString2)
            time.sleep(1)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
        Heart1 = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/ol[1]/li/div/div[2]/div[3]/div[2]/div[3]/button[1]")
        Heart2 = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/ol[1]/li/div/div[2]/div[4]/div[2]/div[3]/button[1]")
        Heart3 = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/ol[1]/li/div/div[2]/div[5]/div[2]/div[3]/button[1]")

        HeartButtons = Heart1 + Heart2 + Heart3
        randomNumber = random.sample(range(0, 9), 3)
        randomNumber.sort()
        for i in range (0, 3):
            try:
                HeartButtons[randomNumber[i]].click()
            except Exception:
                print ("Heart could not be scrolled into view")
