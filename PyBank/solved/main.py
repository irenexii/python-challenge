import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")
total_months = 0
total = 0
changes = []
previous_amount = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""


with open(budget_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        total_months += 1
        date = row[0]
        amount = int(row[1])
        total += amount

        if previous_amount != 0:
            change = amount - previous_amount
            changes.append(change)
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
        
        previous_amount = amount

average = sum(changes) / len(changes)

print(f"Total months: {total_months}")
print(f"Net total amount of Profit/Losses: {total}")
print(f"Average change in Profit/Losses: ${average}")
print(f"The greatest increase in profits: {greatest_increase_date} (${greatest_increase})")
print(f"The greatest increase in profits: {greatest_decrease_date} (${greatest_decrease})")

with open("pybank_results.txt", "w") as file:
    file.write("PyBank Financial Analysis\n")
    file.write("------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${average}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
