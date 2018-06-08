from configparser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')

methods = config.get('methods', 'used').split()

allMethods=[]
for i in range(len(methods)):
    allMethods.append(methods[i])


#allMethods = allMethods.replace(' , ")

__all__ = allMethods
