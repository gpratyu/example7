#!/usr/bin/env python3

import csv
import datetime


# 1. load input.csv into a variable called `polls`
with open('input.csv','r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	polls = [dict(row) for row in rows]

#print(polls)

# 2. write a new file called output.csv and write a row with two headers: "date" and "approve"
with open('output.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['date', 'approve']) 

# 3. Loop through each row of `polls` 
	for poll in polls:
		date = poll['enddate']
		approve = poll['approve']
		#print(date)
		#print(approve)


		# 4. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"
		raw_date = datetime.datetime.strptime(date, "%m/%d/%Y")
		
		date_str = raw_date.strftime("%d-%b-%y") # 01/11/17
		print(date_str)
		
		# 5. write a new row of data with the transformed date and value for "approve" 
		writer.writerow([date_str, approve])





# Anissa and Pratyusha