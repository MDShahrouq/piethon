#!/usr/bin/env python

import urllib
import re
import json
import sys


url = "https://api.github.com/users/"+str(sys.argv[1])

print "Fetching Details of:"+str(sys.argv[1])
print "\nGithub API Url: "+url

request = urllib.urlopen(url).read()

bio = json.loads(request)

#IpAddress = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",request)

#print "My Github profile info is: ",bio
print "\nName:",bio["name"]
print "\nBio:",bio["bio"]
print "\nLocation:",bio["location"]	
print "\nProfile url:",bio["url"]+"\n"
