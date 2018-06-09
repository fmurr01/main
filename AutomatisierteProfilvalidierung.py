import pickle
import time
import random
from random import randint
from selenium import webdriver
from configparser import SafeConfigParser
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from Liker import *
import Liker

config = SafeConfigParser()
config.read('config.ini')

CookieDirectory = config.get('directories', 'cookiedirectory')
ProfileDirectory = config.get('directories', 'profiledirectory')

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

def Loader(driver, StringId, page, directory):
    tld = '.com/'
    if page == 'Bild':
        tld = '.de/'
    driver.maximize_window()
    driver.get('https://' + page + tld)
    cookies = pickle.load(open((directory +StringId+ page+ "Cookies.pkl"),"rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    #driver.set_page_load_timeout(10)
    try:
        driver.get('https://' + page + tld)
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")

####################################################################### end Methods
methods = config.get('methods', 'used').split()
user = config.get('user', 'used').split()

for usr in user:
    print(usr)
    tmpProfile = webdriver.FirefoxProfile(ProfileDirectory + config.get('profiles', usr))
    driver = webdriver.Firefox(firefox_profile=tmpProfile, capabilities=Proxy(config.get('proxy', usr)))

    for mthd in methods:
        page = mthd.replace('Liker','')
        print(mthd)
        Loader(driver, usr, page, CookieDirectory)
        tmp = getattr(Liker, mthd)
        getattr(tmp, mthd)(driver, usr, config.get('interests', usr).split(), CookieDirectory)
        Dumper(driver, usr, page, CookieDirectory)

    driver.quit()
