# import modules
import os
import csv

# Get file path
csvpath = os.path.join("Resources","budget_data.csv")

# Open csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    # Read each row of data after the header
    months = []
    pl = []
    
    # Assign columns to lists by iterating through each row
    for row in csvreader:
        months += [row[0]]
        pl += [float(row[1])]

    n_months = len(months)
    total_pl = sum(pl)
    avg_pl = total_pl/n_months
    min_pl = min(pl)
    min_month = months[pl.index(min_pl)]
    max_pl = max(pl)
    max_month = months[pl.index(max_pl)]

print("Financial Analysis")
print("--------------------------------------------------------------------")
print(f"Total Months: {n_months}")
print(f"Total Profit/Loss: ${total_pl:.0f}")
print(f"Average Profit/Loss: ${avg_pl:.2f}")
print(f"Greatest Increase in Profits: {max_month} (${max_pl:.0f})")
print(f"Greatest Decrease in Profits: {min_month} (${min_pl:.0f})")

f = open("Analysis.txt","w+")
print("Financial Analysis",file=f)
print("--------------------------------------------------------------------",file=f)
print(f"Total Months: {n_months}",file=f)
print(f"Total Profit/Loss: ${total_pl:.0f}",file=f)
print(f"Average Profit/Loss: ${avg_pl:.2f}",file=f)
print(f"Greatest Increase in Profits: {max_month} (${max_pl:.0f})",file=f)
print(f"Greatest Decrease in Profits: {min_month} (${min_pl:.0f})",file=f)


