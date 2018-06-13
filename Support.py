import pickle
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC

#Sets the ip proxy of the profile
def Proxy(proxy):

    desired_capability = webdriver.DesiredCapabilities.FIREFOX
    desired_capability['proxy'] = {
                "proxyType": "manual",
                "httpProxy": proxy,
                "ftpProxy": proxy,
                "sslProxy": proxy
                }
    return desired_capability

#Dumps the new session cookies
def Dumper(driver, StringId, page, directory):
    String = StringId + page + "Cookies.pkl"
    pickle.dump(driver.get_cookies(), open((directory + String),"wb"))
    print('cookies dumped')

#Loads the url of the called method
#Adds/loads the cookies for the driver
def Loader(driver, StringId, page, directory):
    tld = '.com/'
    if page == 'Bild':
        tld = '.de/'
    driver.maximize_window()
    driver.get('https://' + page + tld)
    cookies = pickle.load(open((directory +StringId+ page+ "Cookies.pkl"),"rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    try:
        driver.get('https://' + page + tld)
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
