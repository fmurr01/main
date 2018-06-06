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


CookieDirectory = "C:/Users/Felix Murrenhoff/Desktop/Java/Bachelorarbeit/Cookiefile/"

HannesLocal = 'C:/Users/Felix Murrenhoff/AppData/Roaming/Mozilla/Firefox/Profiles/fz9a3ja0.dev-edition-default'
HannesProxy = "217.61.5.209:3128"
HannesInteressen = ['Fußball','Frankfurt']

DanielLocal = 'C:/Users/Felix Murrenhoff/AppData/Roaming/Mozilla/Firefox/Profiles/p5wq7bed.DanielKraemer'
DanielProxy = "178.238.228.187:9090"
#DanielInteressen = ['Fußball','Frankfurt']

LindaLocal = 'C:/Users/Felix Murrenhoff/AppData/Roaming/Mozilla/Firefox/Profiles/nxhb41z9.LindaMeier'
LindaProxy = "88.99.0.45:3128"
#LindaInteressen = ['Fußball','Frankfurt']

HildegardLocal = 'C:/Users/Felix Murrenhoff/AppData/Roaming/Mozilla/Firefox/Profiles/i0hpiycf.HildegardEvers'
HildegardProxy = "5.189.162.175:3128"
#HildegardInteressen = ['Fußball','Frankfurt']

KaiLocal = 'C:/Users/Felix Murrenhoff/AppData/Roaming/Mozilla/Firefox/Profiles/akj173fm.KaiKrefeld'
KaiProxy = "46.101.157.198:3128"
#KaiInteressen = ['Fußball','Frankfurt']

def Proxy(proxy):

    desired_capability = webdriver.DesiredCapabilities.FIREFOX
    desired_capability['proxy'] = {
                "proxyType": "manual",
                "httpProxy": proxy,
                "ftpProxy": proxy,
                "sslProxy": proxy
                }
    return desired_capability


def CookieDumper(profile, proxy, StringId, page, delay):
    TmpProfile = webdriver.FirefoxProfile(profile)
    TmpDriver = webdriver.Firefox(firefox_profile=TmpProfile, capabilities=Proxy(proxy))
    TmpDriver.get('https://' + page + '.com/')
    time.sleep(delay)
    pickle.dump(TmpDriver.get_cookies() , open((CookieDirectory +StringId+ page+ "Cookies.pkl"),"wb"))
    print('cookies dumped')


CookieDumper(HannesLocal, HannesProxy, "Hannes", "Twitter", 20)
