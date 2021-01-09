import pathlib
import csv

# raw data must be in own file within working directory
csvpath = pathlib.Path("data/budget_data.csv")

# creating empty lists for data to be added to
months = []
profit_change_list = []

with open (csvpath, mode = 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)

    for row in reader:
        months.append(row[0])
        profit_change_list.append(row[1])

#begins the process to export print results to txt file
f = open("output.txt", "w")

""" The following blocks of code grabs and prints summary values
"""

print(f"Financial Analysis", file=f)
print(f"------------------------------", file=f)
# MONTH COUNT
# counts the total months and prints a formatted string with value
total_months = len(months)  
print(f"Total Months: {total_months}", file=f)

# PROFIT/LOSS TOTAL
# sums the total profit/losses and prints formatted string
net_total_list = []

# loops through each number in appended list and turns into int
for num in profit_change_list:
    num = int(num)
    net_total_list.append(num)

# test: print(net_total)
# test: print(sum(net_total))
# sums the total profit/losses and prints formatted string
print(f"Total: ${sum(net_total_list)}", file=f)

# AVERAGE CHANGE
# finds difference between values and appends to new list
list_of_change = []
for i in range(1, len(net_total_list)):
    list_of_change.append(net_total_list[i] - net_total_list[i-1])

# changes new list to ints to prepare for simple operations
int_change_list = []
for num in list_of_change:
    num = int(num)
    int_change_list.append(num)

# finds average profit/loss change and rounds to two decimals
# then prints formatted string with result
average_change = round(sum(int_change_list) / len(int_change_list), 2)
# test: print(average_change)
print(f"Average Change: ${average_change}", file=f)

# GREATEST INCREASE
# the list of changes is shifted one down due to the nature of the operation
# to find the index of the max increase, we have to add one
    # test: print(len(int_change_list))
    # test: print(len(net_total_list))
max_increase = max(int_change_list)
max_index = int_change_list.index(max_increase) + 1
max_month = months[max_index]
# prints results in formatted string
print(f"Greatest Increase in Profits: {max_month} (${max_increase})", file=f)


# GREATEST DECREASE
min_increase = min(int_change_list)
min_index = int_change_list.index(min_increase) + 1
min_month = months[min_index]
# prints results in formatted string
print(f"Greatest Decrease in Profits: {min_month} (${min_increase})", file=f)

f.close()



