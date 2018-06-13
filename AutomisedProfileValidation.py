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
from Support import *

#Load config file
config = SafeConfigParser()
config.read('config.ini')

methods = config.get('methods', 'used').split()
user = config.get('user', 'used').split()

CookieDirectory = config.get('directories', 'cookiedirectory')
ProfileDirectory = config.get('directories', 'profiledirectory')

#This loop creates the profiles and drivers for each user
for usr in user:
    print(usr)
    tmpProfile = webdriver.FirefoxProfile(ProfileDirectory + config.get('profiles', usr))
    driver = webdriver.Firefox(firefox_profile=tmpProfile, capabilities=Proxy(config.get('proxy', usr)))

#the inner loop starts the specified methods from the config
    for mthd in methods:
        page = mthd.replace('Liker','')
        print(mthd)
        Loader(driver, usr, page, CookieDirectory)
        tmp = getattr(Liker, mthd)
        getattr(tmp, mthd)(driver, usr, config.get('interests', usr).split())
        Dumper(driver, usr, page, CookieDirectory)
        
    driver.quit()
