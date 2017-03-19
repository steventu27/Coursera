'''
Exploring the HyperText Transport Protocol
You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look at the response headers:
Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
Use the telnet program as shown in lecture to retrieve the headers and content.
'''

import urllib
import re
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_355886.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('td')
sumlist=list()

for tag in tags:
    a=tag.contents[0]
    aa=str(tag.contents[0])
    num=re.findall('([0-9]*)',aa)
    for i in num:
        if i is not '':
            number=int(i)
            sumlist.append(number) 
print sum(sumlist)
