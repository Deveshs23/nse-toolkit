#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import time
import pyfiglet
from clint.textui import puts,colored,indent
import datetime

datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

new_time = datetime.datetime.now()

web_url = requests.get('https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp').text
soup = BeautifulSoup(web_url, 'lxml')
My_table = soup.find('div',{'class':'opttbldata'})
links = My_table.findAll('a')
df = pd.read_html(str(My_table))

#colors = "38;157;127;"
f = pyfiglet.figlet_format("NSE OPTION CHAIN")
print(colored.blue(f))

#version = pyfiglet.figlet_format("V1.1", font="bubble")
print(colored.green("<---------WELCOME TO NSE OPTION CHAIN--------->"))
print(colored.red("<---------v1.0 - Author - JDeveshJ--------->\n"))
#name = pyfiglet.figlet_format("Devesh", font="digital")
#print(name)

file = input("Enter File name: ")
str(file)

list = ["Chart",'OI','Chng in OI','Volume','IV','LTP','Net Chng',
    'BidQty','BidPrice','AskPrice','AskQty','Strike Price','BidQty',
    'BidPrice','AskPrice','AskQty','Net Chng','LTP','IV','Volume',
    'Chng in OI','OI','Chart']

with open(file, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerows([list])

output_rows = []

i = 1
total_time = 60
enter_time = input("Enter time in Minute: ")

for i in range(total_time):
    for table_row in My_table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)
 
    with open(file, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([new_time])
        writer.writerows([list])
        writer.writerows(output_rows)
        

    time.sleep(60*enter_time)    
