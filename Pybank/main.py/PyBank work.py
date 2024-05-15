#import necessary modules and turn the dataset into a list that can be called on in the code
import pandas as pd  
from datetime import datetime
import os
import csv 
csv_reader = csv.reader(open("Pybank\\resources\\budget_data.csv",'r',encoding= 'UTF-8'))   
csv_list=list(csv_reader)

#create a count of total months and print it
#count the number of dates, remove headers from the count
#create header variables as list of strings for a logical check in the loop
column_headers=(csv_list[0])
datelist=[]    #set empty list to fill with dates
for date , money in csv_list:
    if date in column_headers:
        pass        #if the date is == to a header it will skip, I manually told it what the headers were it does seem reasonable because even table with lots of information will have a manageable number of headers
    else:
        datelist.append(date)    #fill list with dates
print("Total Months:" + " " + str(len(datelist)))             # count the number of entries in that list


#calculate the total of all the entries
#set initial value of 0
totalsum=0
for date, money in csv_list:
    if money not in column_headers: #check to skip colum headers
        totalsum=totalsum +int(money) #add every new value to the initial 0 until end of list
print("Total:" +" " + "$" +str(totalsum))

# Create a dictionary for each row by pairing column headers with values
dict_list=[]
for row in csv_list[1:]:
    row_dict = {column_headers[i]: value for i, value in enumerate(row)}
    dict_list.append(row_dict)

# Initialize a list to store the differences
differences = []

# Iterate over the rows in dict_list
for i in range(len(dict_list) - 1):
    current_value = int(dict_list[i]["Profit/Losses"])
    next_value = int(dict_list[i + 1]["Profit/Losses"])
    difference = next_value - current_value
    differences.append(difference)

# Calculate the average difference
average_difference = sum(differences) // len(differences)

print("Average Change:" + "$" + str(average_difference))

#Find the Maximum Increase
# Initialize variables
current_max_difference = 0

# Iterate over the CSV data, starting from the second entry
for i in range(1, len(csv_list)-1):
    current_entry = csv_list[i]
    next_entry = csv_list[i + 1]

    # Extract money values from current and previous entries
    current_money = int(current_entry[1])
    next_money = int(next_entry[1])

    # Calculate the difference between current and previous money
    difference = next_money-current_money

    # Update current_max_difference if necessary
    if difference > current_max_difference:
        current_max_difference = difference
print("Greatest Increase in Profits:" + " "+ "$" + str(current_max_difference))

# Initialize variables
current_min_difference = 0

# Iterate over the CSV data, starting from the second entry
for i in range(1, len(csv_list)-1):
    current_entry = csv_list[i]
    next_entry = csv_list[i + 1]

    # Extract money values from current and previous entries
    current_money = int(current_entry[1])
    next_money = int(next_entry[1])

    # Calculate the difference between current and previous money
    difference = current_money-next_money

    # Update current_max_difference if necessary
    if difference > current_min_difference:
        current_min_difference = difference
   
print("Greatest Decrease in Profits:" + " " + "-$" + str(current_min_difference))

# Export the analysis results to a text file
with open("financial_analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("-" * 20 + "\n")
    file.write(f"Total Months: {len(datelist)}\n")
    file.write(f"Total: ${totalsum}\n")
    file.write(f"Average Change: ${average_difference}\n")
    file.write(f"Greatest Increase in Profits: ${current_max_difference}\n")
    file.write(f"Greatest Decrease in Profits: ${current_min_difference}\n")

print("Financial analysis results exported to 'financial_analysis.txt'")
