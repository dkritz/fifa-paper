#!/usr/local/bin/python

"""
elomls.py
"""

import csv

with open('2016 MLS Season.csv', 'rb') as csvfile:
     league = csv.reader(csvfile, delimiter=',', quotechar="'")
#     for row in league:
#         print ', '.join(row)
     csvfile.close()



