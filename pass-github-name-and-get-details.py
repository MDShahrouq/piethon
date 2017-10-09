#!/usr/bin/env python

import urllib
import re
import json
import sys
import requests 
#Run this Code , passing Github username Eg, python pass-github-name-and-get-details.py <username>
#to check the Username exists or no
try:
  url = requests.get('https://api.github.com/users/'+str(sys.argv[1]))
  url.raise_for_status()
except requests.exceptions.HTTPError as err:
  print err
  sys.exit(1)

print "\nFetching Details of:"+str(sys.argv[1])
print "\nGithub API Url: "+"https://api.github.com/users/"+str(sys.argv[1])

#request = urllib.urlopen(url).read()
bio = json.loads(url.content)


print "\nName:",bio["name"]
print "\nBio:",bio["bio"]
print "\nLocation:",bio["location"]	
print "\nProfile url:",bio["url"]+"\n"
