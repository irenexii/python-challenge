import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

total_votes = 0
candidate_votes = { }
percentage = 0
winner = ""
max_votes = 0

with open(election_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
        total_amount=sum(candidate_votes.values())

print(f"Total Votes: {total_votes}")
#...............................#

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100

    print(f"{candidate}: {percentage:2.3f}% ({votes})")

    if votes > max_votes:
        max_votes = votes
        winner = candidate

print(f"Winner: {winner}")



with open("pypoll_results.txt", "w") as file:
    file.write("Pypoll Election Results\n")
    file.write("------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {votes} votes ({percentage}%)\n")
    file.write("------------------------\n")

    file.write(f"Winner: {winner}\n")
