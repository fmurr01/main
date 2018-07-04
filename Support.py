# -*- coding: utf-8 -*-
"""The purpose of this module is solely to implement support"""

import pickle
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC

class support():
    """
    This class implements helpful methods for automisedProfileValidation,
    priceWebScraper and cookieDumper
    """

    def proxy(proxy):

        """
        Prepares a DesiredCapabilities object to set as the proxy
        configuration of the used firefox instance and profile

        Args:
            proxy: list of a boolean and the string proxy-ip plus
                port i.e: 94.177.224.181:8080 from the config. The
                Boolean specifies wether a custom proxy is used (True) or not.

        Returns:
            a DesiredCapabilities object containing the desired
            proxy data
        """

        _proxy = proxy.split()
        _desiredCapability = webdriver.DesiredCapabilities.FIREFOX
        if (_proxy[0]=="True"):
            _desiredCapability['proxy'] = {
                        "proxyType": "manual",
                        "httpProxy": _proxy[1],
                        "ftpProxy": _proxy[1],
                        "sslProxy": _proxy[1]
                        }
        else:
            _desiredCapability['proxy'] = {
                    "proxyType": "system"
                    }
        return _desiredCapability


    def dumper(driver, stringId, page, directory):
        """
        Dumps the session cookies in a file named after
        the used profile and visited website into the
        specified location of cookieDirectory

        Args:
            driver: selenium webdriver object (contains profile)
            stringId: string of the name of the firefox-profile
            page: string of the name of the visited page
            directory: directory string
        """

        _string = stringId + page + "Cookies.pkl"
        pickle.dump(driver.get_cookies(), open((directory + _string),"wb"))
        print('cookies dumped')


    def loader(driver, stringId, page, directory):
        """
        Loads the url of the called method and adds/loads the cookies
        for the specified driver and site

        Args:
            driver: selenium webdriver object (contains profile)
            stringId: string of the name of the firefox-profile
            page: string of the name of the visited page
            directory: directory string
        Raises:
            TimeoutException if the site did not load in time
        """

        _tld = '.com/'
        if page == 'Bild':
            _tld = '.de/'
        driver.maximize_window()
        driver.get('https://' + page + _tld)
        _cookies = pickle.load(open((directory +stringId+ page+ "Cookies.pkl"),"rb"))
        for _cookie in _cookies:
            driver.add_cookie(_cookie)
        try:
            driver.get('https://' + page + _tld)
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
