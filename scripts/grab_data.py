import time, datetime
import pandas as pd
import numpy as np

pause = 900 # every fifteen minutes

for i in range(1,96): 
	data = 'https://docs.google.com/spreadsheets/d/18XyBksNbhgcYfyrNneUCZPINJE1oFjsZ0QnJDCFUd6c/export?format=csv&id=18XyBksNbhgcYfyrNneUCZPINJE1oFjsZ0QnJDCFUd6c&gid=711839241'
	
	df = pd.read_csv(data)

	df.columns = ['time', 'tickets','zip']

	df["zip"] = df.zip.map("{:05}".format)

	zipLatLngs = '/Users/danielmsheehan/Dropbox/GIS/Data/National/zipcode/zipcode.csv'

	dfZIP = pd.read_csv(zipLatLngs, dtype={'zip':object})

	df = df.merge(dfZIP, how='left', on='zip')

	print df.head(40)

	df.to_csv('data/magnaball.csv', index=False)
	df.to_csv('/Users/danielmsheehan/Google Drive/magnaball_gdrive.csv', index=False)

	dfTix = df[['tickets']]
	dfg = dfTix.sum()

	x = dfg.head(10)
	print x
	

	print i

	time.sleep(pause)