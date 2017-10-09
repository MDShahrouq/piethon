#!/usr/bin/env python

import urllib
import re

print "To get IP Adress we will run this"

url = "http://checkip.dyndns.org"

print url

request = urllib.urlopen(url).read()

IpAddress = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",request)

print "My IP -Address is =>",IpAddress

