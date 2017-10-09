#!/usr/bin/env python

import urllib
import re
import json


print "To get My Github INfo using Github API"

url = "https://api.github.com/users/mdshahrouq"

print "My Github Profile API : "+url

request = urllib.urlopen(url).read()
bio = json.loads(request)

#IpAddress = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",request)

#print "My Github profile info is: ",bio

print "Bio in Github is :",bio["bio"]

