"""
This is a file
"""

"""
from urllib2 import urlopen as getpage
print = getpage("www.radioreference.com/apps/audio/?ctid=5586")
"""


import csv
import urllib2

url = 'http://winterolympicsmedals.com/medals.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print row


url = 'http://github.com/jokecamp/FootballData/football-data.co.uk/spain/SP1\ (3).csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print row


"""
this didn't work

with open('http://github.com/jokecamp/FootballData/blob/master/football-data.co.uk%2Fspain%2FSP1%20(3).csv') as csvfile:
    sp1 = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in sp1:
        print row[2]
"""
