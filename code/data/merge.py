#!/usr/bin/env python
# coding=utf-8
from __future__ import with_statement 
from argparse import ArgumentParser

import sys
import sqlite3 as lite
import requests
import time
from BeautifulSoup import BeautifulSoup
import dataset
import time
import datetime
from os import listdir
import csv

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]
	


if __name__ == '__main__':
	options = ArgumentParser()
	options.add_argument('-f', '--folder', action='store', dest='folder', help='Provide the folder path of csv')
	options.add_argument('-o', '--output', action='store', dest='output',  help='whats the output csv name?')
	args 	= options.parse_args()
	folder 	= args.folder
	output	= args.output
	column_names = []
	done_once = False
	db = dataset.connect('sqlite:///merge.sqlite')
	db.begin()
	table = db[output]
	all_csv_files = find_csv_filenames(folder)
	for csv_file in all_csv_files:
		all_named_columns = {}
		named_columns = ((csv_file.split("."))[0]).split("__")
		col_no = 0
		for named_column in named_columns:
			all_named_columns["col_no"+str(col_no)] = str(named_column).replace("_", " ")
			col_no = col_no+1
		print "all_named_columns="+str(all_named_columns)
		row_no = 0
		csv_file = str(folder)+"/"+csv_file
		print "csv_file"+str(csv_file)
		with open(csv_file, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for row in reader:
				print ', '.join(row)
				if done_once == False:
					for col in row:
						column_names.append(col)
					done_once = True
					print "Done once the header"
					row_no = row_no + 1
					continue
				if row_no == 0:
					row_no = row_no + 1
					continue
				row_no = row_no + 1
				print "row_no="+str(row_no)
				
				insert_data = {}
				insert_data.update(all_named_columns)
				col_no = 0
				for col in row:
					insert_data[column_names[col_no]] = col
					col_no = col_no+1
				print "insert_data"+str(insert_data)
				table.insert(dict(insert_data))
				db.commit()