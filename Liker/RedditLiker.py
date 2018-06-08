from selenium.common.exceptions import TimeoutException
import time
import random
from random import randint


def RedditLiker(driver, StringId, searchTerms, directory):

    #Loader(driver, StringId, "Reddit", directory)

    for searchTerm in searchTerms:
        searchString = "https://www.reddit.com/search?q=" + searchTerm + "&t=all&sort=new"
        try:
            driver.get(searchString)
            time.sleep(5)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        SubscribeButtons = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/div[4]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/a/div[3]/button")
        lmt = int(len(SubscribeButtons))-1
        try:
            SubscribeButtons[randint(0, lmt)].click()
        except Exception:
            print ("SubscribeButtons could not be scrolled into view")

        LikeButtons = driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div[4]/div/div/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/div/div/div/div[1]/div/button[1]')
        lmt = len(LikeButtons)
        SmallLmt = int(lmt/3)
        randomNumber = random.sample(range(0, lmt), SmallLmt)
        randomNumber.sort()
        for i in range (0, SmallLmt):
            try:
                LikeButtons[randomNumber[i]].click()
            except Exception:
                print ("Like could not be scrolled into view")


    #Dumper(driver, StringId, "Reddit", directory)
