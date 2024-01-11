import os
import csv

#Create variables
profitorloss = []
totalprofitorloss = 0
average = 0
t_months = 0
maxprofit = 0
minprofit = 0
minprofitdate = []
maxprofitdate = []

#create path
csvpath = os.path.join("Resources","budget_data.csv")
txtpath = os.path.join("analysis","budget_analysis.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvtitle = next(csvreader)
    rowfirst = next(csvreader)
    t_months = t_months + 1
    totalprofitorloss += int(rowfirst[1])
    previous = int(rowfirst[1])
    
    #for loop to find month and change
    for row in csvreader:
        t_months = t_months + 1
        totalprofitorloss += int(row[1])
        change = int(row[1]) - previous
        profitorloss.append(change)
        previous = int(row[1])

        #find max and min 
        if change > maxprofit:
            maxprofit = change
            maxprofitdate = row[0]
        if change < minprofit:
            minprofit = change
            minprofitdate = row[0]
            
#average change
average = round(sum(profitorloss) / len(profitorloss), 2)

output = (
    f"Financial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {t_months}\n"
    f"Total: ${totalprofitorloss}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {maxprofitdate} (${maxprofit})\n"
    f"Greatest Decrease in Profits: {minprofitdate} (${minprofit})\n"
)

print(output)
with open(txtpath, "w") as txtfile:
    txtfile.write(output)
