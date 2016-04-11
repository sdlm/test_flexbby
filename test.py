#!/usr/bin/python
# -*- coding: utf-8 -*-

# system
import sys, re

# webparsing
import requests
from bs4 import BeautifulSoup

# helper func
def hasAttrStyle(tag):
	return tag.has_attr('style')

if __name__ == "__main__":
	   
	# check user input
	if len(sys.argv) < 2:
		print '''missing url argument, correct command format: 
    command url'''
		sys.exit(1)

	# get first argument
	url = sys.argv[1]

	# check url
	if not (re.match('^http://', url) or re.match('^https://', url)):
		url = 'http://' + url

	# download pahe
	r = requests.get(url)
	soup = BeautifulSoup(r.text)

	# get all tags with style attribute
	tags = soup.find_all(hasAttrStyle)

	# remove style attribute
	for t in tags:
		del t['style']

	# print results
	print(soup.prettify())