
import pandas as pd
import numpy as np


data = 'https://docs.google.com/spreadsheets/d/18XyBksNbhgcYfyrNneUCZPINJE1oFjsZ0QnJDCFUd6c/export?format=csv&id=18XyBksNbhgcYfyrNneUCZPINJE1oFjsZ0QnJDCFUd6c&gid=711839241'

df = pd.read_csv(data)

df.columns = ['time', 'tickets','zip']

#df['zipcode'] = np.where(df.zip.map(str).len() == 4, '0' + df.zip.map(str), df.zip.map(str))

df["zip"] = df.zip.map("{:05}".format)

zipLatLngs = '/Users/danielmsheehan/Dropbox/GIS/Data/National/zipcode/zipcode.csv'

dfZIP = pd.read_csv(zipLatLngs, dtype={'zip':object})

print df.head(10)

df = df.merge(dfZIP, how='left', on='zip')

print dfZIP.head(1000)

print df.head(40)

df.to_csv('data/magnaball.csv', index=False)
df.to_csv('/Users/danielmsheehan/Google Drive/magnaball_gdrive.csv', index=False)