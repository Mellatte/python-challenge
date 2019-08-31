#depencies
import csv
import os

#file to load and output
csvpath = os.path.join("Resources", "budget_data.csv")
csvoutput = os.path.join("Analysis", "budget_analysis.txt")

#variable 
#track various revenue parameters

total_month = 0 
total_revenue = 0 
previous_revenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change =[]
greatest_increase = ["",0]
greatest_decrease = ["", 999999999999999999]

#read the budget_data.csv file and convert it into a list of dictionaries

with open(csvpath) as revenue_data:
    reader = csv.DictReader(revenue_data)

#loop through the data

for row in reader:

#track the total 
    total_month = total_month + 1
    total_revenue = total_revenue + int(row["Revenue"])

#calculate change of revenue 
    revenue_change = int(row["Revenue"]) - previous_revenue
    previous_revenue = int(row["Revenue"])
    month_of_change = month_of_change + [row["Date"]]
    revenue_change_list = revenue_change_list + [revenue_change]

#calculate the greatest increase
    if (revenue_change > greatest_increase[1]):
        greatest_increase[0] = row["Date"]
        greatest_increase[1] = revenue_change

#calculate the greatest decrease
    if (revenue_change < greatest_decrease[1]):
        greatest_decrease[0] =row["Date"]
        greatest_decrease[1] = revenue_change

# calculate the avrage revenue change
revenue_avg = sum(revenue_change_list)/len(revenue_change_list)

# print output summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months : {total_month}\n"
    f"Total Revenue : ${total_revenue}\n"
    f"Average Revenue Chnange : ${revenue_avg}\n"
    f"Greatest increase in Revenue : {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"Greatest decrease in Revenue : {greatest_decrease[0]} ${greatest_decrease}\n"
)

#print the output to terminal
print(output)

#export/write the restult to text file
with open(csvoutput, 'w') as txt_file:
    txt_file.write(output)









