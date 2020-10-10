import pandas as pd
import os
import csv

def input_tcsv(filename):
	fn = len(filename)
	print("Input  : " + filename)
	with open(filename, mode='r') as f:
		s = f.read().replace(', "', ',"')
		with open('mid.csv', mode='w') as fcsv:
			fcsv.write(s)
	with open('mid.csv') as f:
		reader = csv.reader(f)
		with open('in.csv', 'w') as fw:
			writer = csv.writer(fw)
			writer.writerows(reader)
	os.remove('mid.csv')
	df = pd.read_csv('in.csv',dtype='str')
	os.remove('in.csv')
	return df