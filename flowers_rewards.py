#!/usr/local/bin/python3
# meant to be run with Python 3; tested with Python 3.3.3

# flowers_rewards.py
# (c) 2013 Bonnie Schulkin
# franken-script modifications (c) 2015 Victoria Angel

# This script is used to upload test mobile reward_pass events for 1800flowers

############
# includes #
############

from urllib.request import urlopen, Request, ContentTooShortError
from urllib.error import HTTPError, URLError
from urllib.parse import quote
import json, os
import time

# for exception reporting
from traceback import format_exc

# for making random email addresses
import random
import string

# for making md5 hashes for security
import hashlib

##import ff loyalty##
import sys
sys.path.append('/Users/vangel/Documents/ffloyalty_api/python 3')
sys.path.append('/Users/vangel/Documents/ffloyalty_api/python 3')
from FFloyalty import FFloyalty


#############
# constants # 
#############

UUID = 'Clj4byLBGxzZJIT'
SECRET_KEY = 'wh1mD3OzZoNkI6mWK3Wva12YlcGPbCly'
ENV = 'production'
ffl = FFloyalty(UUID, SECRET_KEY, env=ENV, debug=False, exec_api=True)

#############
# functions #
#############


######Get List######
def get_list(filename): 
	scriptDir = os.path.dirname(os.path.realpath(__file__))
	with open(os.path.join(scriptDir, filename)) as f:
		lines = f.read()
		f.close()
	return lines.split('\n')	


# Member Email,Reward Pass Number,PIN,Value,Expiration Date
datalist=get_list("flowers_member.txt")
detail_template = "Your {value} Reward Pass Number: {number} PIN: {pin}, expires on: {date}"

for item in datalist[0:1]:

	# Your $20.00 Reward Pass Number: 6035710369309437796 PIN: 6000, expires on: 9/3/15
	
	tokens = item.split(',')
	
	
	args = {}
	args['email'] = tokens[0]
	args['type'] = "rewards_pass"
# 	args['detail'] = tokens[2]
	args['detail'] = detail_template.format(number=tokens[1], pin=tokens[2], value=tokens[3], date=tokens[4])
	args['expires_at'] = '12/31/2017T23:59:59'
	print (detail_template.format(number=tokens[1], pin=tokens[2], value=tokens[3], date=tokens[4]))
	#exit()

	jsondict = ffl.run('/api/record.json', args)

	if not jsondict['success']:
		print ("item failed: " + item)
		print(str(jsondict))
		print('')