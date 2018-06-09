import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from configparser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')

CookieDirectory = config.get('directories', 'cookiedirectory')
ProfileDirectory = config.get('directories', 'profiledirectory')

def Proxy(proxy):

    desired_capability = webdriver.DesiredCapabilities.FIREFOX
    desired_capability['proxy'] = {
                "proxyType": "manual",
                "httpProxy": proxy,
                "ftpProxy": proxy,
                "sslProxy": proxy
                }
    return desired_capability


def CookieDumper(StringID ,page, delay):
    TmpProfile = webdriver.FirefoxProfile(ProfileDirectory + config.get('profiles', StringID))
    TmpDriver = webdriver.Firefox(firefox_profile=TmpProfile, capabilities=Proxy(config.get('proxy', StringID)))
    TmpDriver.get('https://' + page + '.com/')
    time.sleep(delay)
    pickle.dump(TmpDriver.get_cookies() , open((CookieDirectory +StringID+ page+ "Cookies.pkl"),"wb"))
    print('cookies dumped')


CookieDumper("Kai", "Google", 3)
