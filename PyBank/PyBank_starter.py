# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = [0]
total_net = [1]
# Add more variables to track other necessary financial data
profits_losses = []
change  = []
average_change = []
Greatest_Inc_Profits = []
Greatest_Dec_Profits = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")
with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    row_count = sum(1 for row in csvreader)  # Count each row
print(f'Total Months: {row_count - 1}') #count rows and remove header row

total_net = 0
with open('budget_data.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile)
    header =next(csvreader)
    for row in csvreader:
        total_net += float(row[1])
print("Total net: $", total_net)

    # Extract first row to avoid appending to net_change_list
average_change = int(row[1])
#with open('budget_data.csv', 'r') as csvfile:
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")
    with open('budget_data.csv', 'r') as csvfile:
        header = next(financial_data)
        for row in financial_data:
                financial_data['Change'] = financial_data['Profit/Losses'].diff()
                average_change = financial_data['Change'].mean()
print(f"Average Change: ${average_change:.2f}")
         

    # Track the total and net change
    

    # Process each row of data
 

        # Track the total


        # Track the net change


        # Calculate the greatest increase in profits (month and amount)
#Greatest_Inc_Profits = ["", 0]

        # Calculate the greatest decrease in losses (month and amount)
#Greatest_Dec_Profits = ["", 0]


# Calculate the average net change across the months


# Generate the output summary


# Print the output
    #file_to_output = os.path.join(PyBank_Final.csv)
# OR-----maybe this is *below*
# file_to_output = (f"Financial Analysis"\n"
#           -------------------------,
#          f"Total Months: {total_months}\n"
#          f"Total: {total_net:,}\n" *add format for $$
#          f"Average Change: {average_change:,}\n" *add formate for $$
#          f"Greatest Increase in Profits: {Greatest_Inc_Profits:,}\n" **add format for $$
#          f"Greatest Decrease in Profits: {Greatest_Dec_Profits:,}")" **add format for $$
#print(file_to_output)

# Write the results to a text file
#with open(file_to_output, "w", newline=' ') as txt_file:
   #txt_file.write(output)
