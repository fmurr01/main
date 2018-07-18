# -*- coding: utf-8 -*-
"""The purpose of this module is to implement youtubeLiker"""

import pickle
import time
from selenium import webdriver
from configparser import SafeConfigParser
from support import *

class CookieDumper():

    def cookieDumper(stringIDs, pages, delay):
        """
        The cookieDumper helps dumping session cookies for each profile. The persistent cookies are saved in the Firefox profiles.
        Dumping session cookies will help logging into the websites and is mandatory for automisedProfileValidation to work.
        This method only has to be used the first time.

        Args:
            stringIDs: string Array of the names of the profiles
            pages: set for which pages cookies should be saved
            delay: set a timer until the cookies get dumped (you will need to log-in within that timeframe)

        Returns: Cookiefile (.pkl) like 'stringID + page + Cookies.pkl'
        """
        _config = SafeConfigParser()
        _config.read('config.ini')

        _cookieDirectory = _config.get('directories', 'cookieDirectory')
        _profileDirectory = _config.get('directories', 'profileDirectory')
        for _usr in stringIDs:
            _tmpProfile = webdriver.FirefoxProfile(_profileDirectory + _config.get('profiles', _usr))
            _tmpDriver = webdriver.Firefox(firefox_profile=_tmpProfile, capabilities=support.proxy(_config.get('proxy', _usr)))
            for _p in pages:
                _tmpDriver.get('https://' + _p)
                time.sleep(delay)
                _p = _p.title()
                pickle.dump(_tmpDriver.get_cookies() , open((_cookieDirectory +_usr+ _p+ "Cookies.pkl"),"wb"))
                print('cookies dumped')
            _tmpDriver.quit()

"""
Select the profile you want to dump cookies for and the website. Then choose a delay that allows you
to log into the profile account on that website. After the delay the cookies will be dumped.
Clicking on Browser options like "Save this password" will save the log-in cookies in the Firefox profile.
Which allows you to log-in without loading the session cookies and you can choose a very short delay.
"""

CookieDumper.cookieDumper(["Hannes", "Daniel", "Linda", "Hildegard"], ["cyberport.de", "esprit.de", "zalando.de", "mediamarkt.de", "amazon.de", "tchibo.de", "otto.de"], 1)
