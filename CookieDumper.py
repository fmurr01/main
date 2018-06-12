import pickle
import time
from selenium import webdriver
from configparser import SafeConfigParser
from AutomisedProfileValidation import Proxy

#The CookieDumper helps dumping session cookies for each profile. The persistent cookies are saved in the Firefox profiles.
#Dumping session cookies will help logging into the websites and is mandatory for AutomisedProfileValidation to work.
config = SafeConfigParser()
config.read('config.ini')

CookieDirectory = config.get('directories', 'cookiedirectory')
ProfileDirectory = config.get('directories', 'profiledirectory')

def CookieDumper(StringID ,page, delay):
    TmpProfile = webdriver.FirefoxProfile(ProfileDirectory + config.get('profiles', StringID))
    TmpDriver = webdriver.Firefox(firefox_profile=TmpProfile, capabilities=Proxy(config.get('proxy', StringID)))
    TmpDriver.get('https://' + page + '.com/')
    time.sleep(delay)
    pickle.dump(TmpDriver.get_cookies() , open((CookieDirectory +StringID+ page+ "Cookies.pkl"),"wb"))
    print('cookies dumped')

#Select the profile you want to dump cookies for and the website. Then choose a delay that allows you
#to log into the profile account on that website. After the delay the cookies will be dumped.
#Clicking on Browser options like "Save this password" will save the log-in cookies in the Firefox profile.
#Which allows you to log-in without loading the session cookies and you can choose a very short delay.
CookieDumper("Kai", "Google", 3)
