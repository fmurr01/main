import pickle
import time
import random
from random import randint
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CookieDirectory = "C:/Users/Felix Murrenhoff/Desktop/Java/Bachelorarbeit/Cookiefile/"
ProfileDirectory = "C:/Users/Felix Murrenhoff/AppData/Roaming/Mozilla/Firefox/Profiles/"

HannesLocal = ProfileDirectory + 'fz9a3ja0.dev-edition-default'
HannesProxy = "217.61.5.209:3128"
HannesInteressen = ['Fußball','Frankfurt']

DanielLocal = ProfileDirectory + 'p5wq7bed.DanielKraemer'
DanielProxy = "178.238.228.187:9090"
#DanielInteressen = ['Fußball','Frankfurt']

LindaLocal = ProfileDirectory + 'nxhb41z9.LindaMeier'
LindaProxy = "88.99.0.45:3128"
#LindaInteressen = ['Fußball','Frankfurt']

HildegardLocal = ProfileDirectory + 'i0hpiycf.HildegardEvers'
HildegardProxy = "5.189.162.175:3128"
#HildegardInteressen = ['Fußball','Frankfurt']

KaiLocal = ProfileDirectory + 'akj173fm.KaiKrefeld'
KaiProxy = "46.101.157.198:3128"
#KaiInteressen = ['Fußball','Frankfurt']

####################################################################### start Methods
def Proxy(proxy):

    desired_capability = webdriver.DesiredCapabilities.FIREFOX
    desired_capability['proxy'] = {
                "proxyType": "manual",
                "httpProxy": proxy,
                "ftpProxy": proxy,
                "sslProxy": proxy
                }
    return desired_capability

def Dumper(driver, StringId, page, directory):
    String = StringId + page + "Cookies.pkl"
    pickle.dump(driver.get_cookies(), open((directory + String),"wb"))
    print('cookies dumped')

def Loader(driver, StringId, page):
    driver.maximize_window()
    driver.get('https://' + page + '.com/')
    cookies = pickle.load(open(("C:/Users/Felix Murrenhoff/Desktop/Java/Bachelorarbeit/Cookiefile/" +StringId+ page+ "Cookies.pkl"),"rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    #driver.set_page_load_timeout(10)
    try:
        driver.get('https://' + page + '.com/')
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")

def TwitterLiker(driver, StringId, searchTerms):

    #Loader(driver, StringId, "Twitter")
    for searchTerm in searchTerms:
        searchString = "https://twitter.com/search?q=" + searchTerm + "&src=typd"
        try:
            driver.get(searchString)
            time.sleep(1)
            print("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        FollowButtons = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/ol[1]/li[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div/span[2]/button[1]")
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

        print(len(HeartButtons))
        randomNumber = random.sample(range(0, 9), 3)
        randomNumber.sort()
        for i in range (0, 3):
            try:
                HeartButtons[randomNumber[i]].click()
            except Exception:
                print ("Heart could not be scrolled into view")

    Dumper(driver, StringId, "Twitter", CookieDirectory)

def FacebookLiker(driver, StringId, searchTerms):

    #Loader(driver, StringId, "Facebook")

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

        PageLikeButtons = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[3]/div/div/div/div[2]/div/div[3]/div/div/div/div/div/div/div[3]/div[1]/div[2]/span[1]/span[1]')
        try:
            PageLikeButtons[randint(0, 2)].click()
        except Exception:
            print ("PageLikeButtons could not be scrolled into view")

        LikeButtons2 = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[3]/div/div/div/div[2]/div/div[3]/div/div/div/div/div/div/div[3]/div[2]/form/div[1]/div/div/div/div[2]/div/div/span[1]")
        for btn in LikeButtons2:
            try:
                btn.click()
            except Exception:
                print ("Follow could not be scrolled into view")

    Dumper(driver, StringId, "Facebook", CookieDirectory)

def RedditLiker(driver, StringId, searchTerms):

    #Loader(driver, StringId, "Reddit")

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


    Dumper(driver, StringId, "Reddit", CookieDirectory)

def YoutubeLiker(driver, StringId, searchTerms):

    #Loader(driver, StringId, "Youtube")

    for searchTerm in searchTerms:
        searchString = "https://www.youtube.com/results?search_query=" + searchTerm
        try:
            driver.get(searchString)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        VideoButtons = driver.find_elements_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[3]/ytd-item-section-renderer/div[2]/ytd-video-renderer")
        VideoButtons[randint(0, 19)].click()
        time.sleep(30) #validate view

        LikeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]")
        DislikeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]")
        LikeButton.click()
        time.sleep(15) #validate view

    driver.back()
    Dumper(driver, StringId, "Youtube", CookieDirectory)

def BildReader(driver, StringId, searchTerms):
    driver.maximize_window()
    driver.get('https://www.bild.de/')
    cookies = pickle.load(open((CookieDirectory +StringId+ "Bild"+ "Cookies.pkl"),"rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    #driver.set_page_load_timeout(10)
    try:
        driver.get("https://www.bild.de/")
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")

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

    Dumper(driver, StringId, "Bild", CookieDirectory)

def Start(profile, StringId, searchTerms, proxy):
    tmpProfile = webdriver.FirefoxProfile(profile)
    driver = webdriver.Firefox(firefox_profile=tmpProfile) #, capabilities=Proxy(proxy))
    TwitterLiker(driver, StringId, searchTerms)
    FacebookLiker(driver, StringId, searchTerms)
    RedditLiker(driver, StringId, searchTerms)
    BildReader(driver, StringId, searchTerms)
    YoutubeLiker(driver, StringId, searchTerms)
    driver.quit()
####################################################################### end Methods

Start(HannesLocal, "Hannes", HannesInteressen, HannesProxy)
