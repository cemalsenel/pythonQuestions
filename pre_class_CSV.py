""" 
Working with the CSV Files
You have earned 0 point(s) out of 0 point(s) thus far.
Ordinary Reading Method of CSV Files
This method is quite simple and does not differ from reading the text files.

with open("fruits.csv", 'r', encoding="utf-8") as file:
    print(file.read())

output:
no,fruit,amount
1,Banana,4 lb
2,Orange,5 lb
3,Apple,2 lb
4,Strawberry,6 lb
5,Cherry,3 lb

"""
with open("fruits.csv", 'r', encoding="utf-8") as file:
    print(file.read())

""" 
Reading the CSV Files with 'csv' Module
Since the content of the CSV files is displayed in a more readable and regular format with this method, 
this method is more preferred than the previous one.

First of all, of course, we should load csv module. 
Secondly, we will use csv.reader() function in a for loop to read the CSV file. 
Examine the following example carefully :
"""
import csv  # loads csv module

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file)  # reader() function takes each
                                 # row (lines) into a list
    for row in csv_rows: 
        print(row) 
""" 
['no', 'fruit', 'amount']
['1', 'Banana', '4 lb']
['2', 'Orange', '5 lb']
['3', 'Apple', '2 lb']
['4', 'Strawberry', '6 lb']
['5', 'Cherry', '3 lb']
As you can see, the rows are displayed in the list type. 
Each element of the rows is located as separate strings in the list. 
There are three strings in each list.

Tips:
If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on platforms that use \r\n linendings on write an extra \r will be added.
It is best practice and always safe to specify newline='', since the csv module does its own newline handling.

The default value of the delimiter parameter is ",". Thus, we can display each comma-separated element as separate strings. At this time let's use the delimiter="," parameter and see the same result as the previous one.
"""
import csv

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file, delimiter= ",")  # gives the same output as the previous one
                                 
    for row in csv_rows: 
        print(row) 
""" 
['no', 'fruit', 'amount']
['1', 'Banana', '4 lb']
['2', 'Orange', '5 lb']
['3', 'Apple', '2 lb']
['4', 'Strawberry', '6 lb']
['5', 'Cherry', '3 lb']

We can also display each row in the list as a single string. 
If we determine a character that is not included in the CSV file and allocate this character 
as the value of delimiter, we can print all lines of the CSV file as lists as a single string element. 
Consider this one :
"""
import csv 

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file, delimiter = ':')  # we specified a char ":" that is not used
                                                  # in the csv file as a value of delimiter
    for row in csv_rows: 
        print(row)   
""" 
['no,fruit,amount']
['1,Banana,4 lb']
['2,Orange,5 lb']
['3,Apple,2 lb']
['4,Strawberry,6 lb']
['5,Cherry,3 lb']
Yes, we got another list type output. Unlike the previous one, each row (list) contains a single string.
"""