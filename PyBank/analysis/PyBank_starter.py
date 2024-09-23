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
profits_losses = [1]
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

total_net = 0
profits_losses = []  # List to store changes
previous_value = None  # To track the previous month's value
# Open and read the CSV file
with open('budget_data.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row
    # Loop through the rows
    for row in csvreader:
        current_value = int(row[1])  # Get current month's profit/loss
        if previous_value is not None:
            # Calculate the change from the previous month
            change = current_value - previous_value
            profits_losses.append(change)  # Append to the list of changes
        previous_value = current_value  # Update previous value for the next iteration
        # Add the profit/loss to total_net
        total_net += current_value
# Ensure that profits_losses contains values before computing the average
if len(profits_losses) > 0:
    average_change = sum(profits_losses) / len(profits_losses)
else:
    average_change = 0  # If no changes, default to 0

# Reset previous_value and open the file to calculate greatest increase
previous_value = None
greatest_increase_month = [0]
greatest_increase = ["", 0]  # Store month and amount of the greatest increase
with open('budget_data.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row
    for row in csvreader:
        current_value = int(row[1])
        # Calculate the change from the previous month (if not the first month)
        if previous_value is not None:
            change = current_value - previous_value
            # Check if the current change is the greatest increase
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
        # Update previous_value for the next iteration
        previous_value = current_value
# Now greatest_increase will hold the correct month and amount
print(f"Average Change: ${average_change:.2f}")

print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")

previous_value = None
greatest_decrease_month = [0]
greatest_decrease = ["", 0] # Store month and amount of the greatest increase
with open('budget_data.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row
    for row in csvreader:
        current_value = int(row[1])
        # Calculate the change from the previous month (if not the first month)
        if previous_value is not None:
            change = current_value - previous_value
            # Check if the current change is the greatest increase
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        # Update previous_value for the next iteration
        previous_value = current_value

print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


# Print the output
#file_to_output = os.path.join(PyBank_Final.csv)

file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Write the results to a text file
with open(file_to_output, "w", newline=' ') as txt_file:
   txt_file.write(output)
