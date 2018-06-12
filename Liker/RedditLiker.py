from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint

#This method is responsible for automising reddit activity. It receives the driver(the webdriver that runs firefox)
#the name of the user (StringId) and the interests of the user (search terms)
def RedditLiker(driver, StringId, searchTerms):

#Each serch term is being used in the reddit search by adding it to the URL.
#Then 2 of the 3 shown subscribe options will be clicked and 1/3 of all shown inserations liked.
#There are a bunch of sleeps, because even though ".get" waits for the entire page to load,
#Sometimes the buttons load a little bit later. Also it fakes real behaviour better.
    for searchTerm in searchTerms:
        searchString = "https://www.reddit.com/search?q=" + searchTerm + "&t=all&sort=new"
        try:
            driver.get(searchString)
            time.sleep(2)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        SubscribeButtons = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/a/div[3]/button")
        try:
            randomNumber = random.sample(range(0, 3), 2)
            randomNumber.sort()
            SubscribeButtons[randomNumber[0]].click()
            time.sleep(1)
            SubscribeButtons[randomNumber[1]].click()
            time.sleep(1)
        except Exception:
            print ("SubscribeButtons could not be scrolled into view")

        LikeButtons = driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/div/div/div/div[1]/div/button[1]')
        lmt = len(LikeButtons)
        SmallLmt = int(lmt/3)
        randomNumber = random.sample(range(0, lmt), SmallLmt)
        randomNumber.sort()
        for i in range (0, SmallLmt):
            try:
                LikeButtons[randomNumber[i]].click()
            except Exception:
                print ("Like could not be scrolled into view")
