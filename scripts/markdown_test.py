
headerInfo = """---
layout: post
title:  "Magnaball Ticket Need Stats"
date:   2015-08-17 19:36:07
categories: jekyll update
---"""
text_file = open('/Users/danielmsheehan/GitHub/magnaball.github.com/_posts/2015-08-17-magnaball-stats.markdown', "w")
x = x.replace('dtype: int64','').replace('tickets','')

theText = headerInfo +'\n'+ '\n' + 'The number of tickets people want is: <strong>' + x + '</strong>' + '\n' + '\n' + 'Ticket count not updated as frequently as map.'
text_file.write(theText)
text_file.close()

print theText