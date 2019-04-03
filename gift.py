#!/usr/local/bin/python3
# meant to be run with Python 3; tested with Python 3.3.3

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

UUID = 'zzH8aExEjWHnY3x'
SECRET_KEY = 'HinMeTNDJcX5i90FzdG1oKsgU73afVlt'
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


# Member List
datalist=get_list("members.txt")

for item in datalist[0:]:

	tokens = item.split(',')

	args = {}
	args['email'] = tokens[0]
	args['type'] = tokens[1]
	args['detail'] = tokens[2]
	args['event_id'] = tokens[3] + '0222gift'
	args['value'] = tokens[4]
	args['expires_at'] = '2020-02-19'
	
	

	
	jsondict = ffl.run('/api/record.json', args)

	if not jsondict['success']:
		print ("item failed: " + item)
		print(str(jsondict))
		print('')
		
		with open('errors.txt','a') as f:	
			print ("item failed: " + item, file=f)
	
	else:
		print ("item success: " + item)
		print(str(jsondict))
		print('')
		
		with open('success.txt','a') as f:	
			print ("item Success: " + item, file=f)