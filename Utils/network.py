# import time
# import urllib.request
# import urllib.parse
#
# def login(username, password):
#     url="http://10.108.255.249/include/auth_action.php"
#     data={"username": username,
#           "password": password,
#           "action": "login",
#           "ac_id": 1,
#           "ajax": 1}
#     data = urllib.parse.urlencode(data)
#     urllib.request.urlopen(url, data)
#
#
# username = "shran"
# password = "ranshihan"
#
#
# while True:
#     try:
#         login(username, password)
#     except:
#         print('Fail...')
#         pass
#     time.sleep(300)

# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
#__author__= 'ihciah@gmail.com'

import urllib, urllib2, time

def login(username, password):
    url="http://10.108.255.249/include/auth_action.php"
    data={"username": username,
          "password": password,
          "action": "login",
          "ac_id": 1,
          "ajax": 1}
    data=urllib.urlencode(data)
    urllib2.urlopen(url, data)

username="15307130424"
password="caroline970505"

while True:
    try:
        login(username, password)
    except:
        print 'Fail...'
        pass
    time.sleep(300)
