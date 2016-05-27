import urllib
import urllib2
import cookielib
import re
import csv
import codecs
from bs4 import BeautifulSoup
import numpy as np
import math
import matplotlib.pyplot as plt

ecs20 = 'http://nook.cs.ucdavis.edu/~koehl/Teaching/ECS20/grades.html'
req = urllib2.Request(ecs20)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'lxml')


tablelist = soup.findAll('table', align="left", border="1" , cellpadding="3")

td_th = re.compile('t[dh]')
mid1 = []
mid2 = []
for table in tablelist:
	for row in table.findAll("tr"):
	    cells = row.findAll(td_th)
	    if "Student ID (4 last digits)" == cells[0].find(text=True):
	    	continue
	    mid1.append(cells[2].find(text=True))
	    mid2.append(cells[3].find(text=True))

	    
midone = [int(x) for x in mid1 if x != None and x != 0]
midtwo = [int(x) for x in mid2 if x != None and x != 0]

print sum(midtwo)/len(midtwo)
print math.sqrt(np.var(midtwo))
print sum(midone)/len(midone)
print math.sqrt(np.var(midone))
#plt.scatter(midone,midtwo)
a = [0]*77
b = [i for i in range(0,77)]
c = []
d = []
e = [66]*77
f = [63]*77
g = [55]*77
plt.axis([0,76,0,12])
for i in midtwo:
	a[i] = a[i] + 1
for i in range(0,len(a)):
	if a[i] != 0:
		c.append(a[i])
		d.append(b[i])
#plt.scatter(d,c)
#plt.plot(d,c)
#plt.plot(e,b)
#plt.plot(f,b)
#plt.plot(g,b)
m = [66]*a[66]
plt.hist(midtwo,range(0,78))
plt.hist(m, width = 1,color = 'r')
plt.show()