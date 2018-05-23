#!/usr/bin/python

import re

str = "Hello from Ram"
store = re.compile('Hello')
find = store.match(str)
#print(find)
if find:
    print('given string matched', find.group(), find.span())
else:
    print('No match')
