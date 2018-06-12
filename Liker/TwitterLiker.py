from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint

#This method is responsible for automising twitter activity. It receives the driver(the webdriver that runs firefox)
#the name of the user (StringId) and the interests of the user (search terms)
def TwitterLiker(driver, StringId, searchTerms):

#Each serch term is being used in the twitter search by adding it to the URL.
#On that page the shown users will receive a follow.
#To get newer tweets we jump to the "new" page and randomly like 3 shown tweets.
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
                print ("Already Followed/Follow could not be scrolled into view")

        searchString2 = "https://twitter.com/search?f=tweets&vertical=news&q=" + searchTerm + "&src=typd"
        try:
            driver.get(searchString2)
            time.sleep(1)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
        HeartButtons = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/ol[1]/li/div/div[2]/div/div[2]/div[3]/button[1]")
        randomNumber = random.sample(range(0, 9), 3)
        randomNumber.sort()
        for i in range (0, 3):
            try:
                HeartButtons[randomNumber[i]].click()
            except Exception:
                print ("Heart could not be scrolled into view")
