# -*- coding: utf-8 -*-
"""
The purpose of this module is to alter the *-statement for the liker folder,
so it only includes modules specified in the config
"""

from configparser import SafeConfigParser

_config = SafeConfigParser()
_config.read('config.ini')

_methods = _config.get('methods', 'used').split()

_allMethods=[]
for i in range(len(_methods)):
    _allMethods.append(_methods[i])

__all__ = _allMethods
