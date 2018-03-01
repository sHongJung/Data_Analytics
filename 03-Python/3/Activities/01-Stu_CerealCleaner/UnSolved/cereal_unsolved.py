""" Cereal Reader

## Instructions

* Read through the csv of cereals.

* Find all the cereals with 5 grams of fiber or more.

  * Fiber is column H in your csv.

* Print those out to your terminal

## Hint

* Everything in the csv is stored as a string and certain rows have a decimal. How can we convert these to a float?

## Bonus

* Try the following again but this time using the `cereal.csv` which has a header included in the file."""

import csv
import os

csvpath = os.path.join('Resources', 'cereal.csv')
csvfile = open(csvpath, 'r', encoding = 'utf-8')

rdr = csv.reader(csvfile)

for line in rdr:
	print(line)

csvfile.close()