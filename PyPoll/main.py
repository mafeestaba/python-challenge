import os
import csv

# Create Variables
candidates = []
candidate = ""
winner = ""
votes = 0
total_votes = 0
candidate_votes = {}
max_votes = 0
winners = 0

csvpath = os.path.join("Resources", "election_data.csv")
txtpath = os.path.join("analysis", "election_analysis.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvtitle = next(csvreader)

    # Loop through each vote
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]


        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0

        candidate_votes[candidate] = candidate_votes[candidate]+1

with open(txtpath, "w") as txtfile:

    output = (
        f"Election Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------\n")
    print(output)
    txtfile.write(output)

#For loop to print candidates with each amount of votes
    for x in candidate_votes:
        votes = candidate_votes.get(x)
        votes_per = float(votes)/float(total_votes) * 100
        if (votes>winners):
            winners = votes
            winner = x

        output = (
            f"{x}: {votes_per:.3f}% ({votes})\n")
        print(output)
        txtfile.write(output)

    output=(
        f"---------------------\n"
        f"Winner: {winner}\n"
        f"---------------------\n")
    print(output)
    txtfile.write(output)
