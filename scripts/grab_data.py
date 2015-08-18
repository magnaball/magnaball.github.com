import time, datetime
from datetime import datetime
import pandas as pd
import numpy as np

pause = 360 # every 6 minutes

for i in range(1,300): 
	data = 'https://docs.google.com/spreadsheets/d/18XyBksNbhgcYfyrNneUCZPINJE1oFjsZ0QnJDCFUd6c/export?format=csv&id=18XyBksNbhgcYfyrNneUCZPINJE1oFjsZ0QnJDCFUd6c&gid=711839241'
	
	df = pd.read_csv(data)#, dtype={'zip':object})

	df.columns = ['time', 'tickets','zip']

	#df['zip'] = df.zip.map(str)
	#df['zip'] = df.zip.str[:5] #FIX THIS IS TEMPORARY FOR CANADIAN ADDRESSES THAT ARE 6 DIGITS
	df["zip"] = df.zip.map("{:05}".format)
	df['zip'] = df.zip.map(str).replace('.0','')

	zipLatLngs = '/Users/danielmsheehan/Dropbox/GIS/Data/National/zipcode/zipcode.csv'

	dfZIP = pd.read_csv(zipLatLngs, dtype={'zip':object})
	#print dfZIP.head(40)

	df = df.merge(dfZIP, how='left', on='zip')

	#print df.head(10)

	df.to_csv('data/magnaball.csv', index=False)
	df.to_csv('/Users/danielmsheehan/Google Drive/magnaball_gdrive.csv', index=False)

	dfTix = df[['tickets']]
	dfg = dfTix.sum()

	x = dfg.head(10)
	
	x = ''.join(map(str,x))

	headerInfo = """---
layout: post
title:  "Magnaball Ticket Need Stats"
date:   2015-08-18 05:36:07
categories: magnaball
---"""

	text_file = open('/Users/danielmsheehan/GitHub/magnaball.github.com/_posts/2015-08-18-magnaball-stats.markdown', "w")
	x = x.replace('dtype: int64','').replace('tickets','')

	y = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	z = int(x) * 225

	theText = headerInfo +'\n'+ '\n' + 'The number of tickets people want is: <strong>' + x + '</strong>' + '\n' + '\n' + 'Ticket count may not updated as frequently as map. Updated as of '+y+ ' EST.' + '\n' + '\n' +'At $225 a ticket, that would be <strong>$' + str(z) + '</strong> in GA tickets.'
	text_file.write(theText)
	text_file.close()

	print theText

	print i
	print datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	time.sleep(pause)