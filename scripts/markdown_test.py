
headerInfo = """---
layout: post
title:  "Magnaball Ticket Need Stats"
date:   2015-08-17 19:36:07
categories: jekyll update
---"""



text_file = open('/Users/danielmsheehan/GitHub/magnaball.github.com/_posts/2015-08-17-magnaball-stats.markdown', "w")

x = """tickets    98
dtype: int64"""

theText = headerInfo +'\n'+ '\n' + x

text_file.write(theText)
text_file.close()