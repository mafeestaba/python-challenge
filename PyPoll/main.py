import os
import csv

candidates = []
candidate = ""
winner = []
votes = 0
total_votes = 0
candidate_votes = {}

csvpath = os.path.join("Resources", "election_data.csv")
txtpath = os.path.join("analysis", "election_analysis.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvtitle = next(csvreader)

    for row in csvreader:
        total_votes = total_votes +1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate]=0

        candidate_votes[candidate] = candidate_votes[candidate]+1


        #voters.append(row[0])
        



with open(txtpath, "w") as txtfile:

    output = (
        f"Election Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------\n")
    print(output)
    txtfile.write(output)

    for x in candidates:
        votes = candidate_votes.get(x)
        votes_per = float(votes)/float(total_votes) * 100
        output=(f"{x}: {votes_per:.3f}% ({votes}) \n")
        print(output)
        txtfile.write(output)


    #     f"Charles Casper Stockham: {candidate}\n"
    #     f"Diana DeGette: {(votes)}\n"
    #     f"Raymon Anthony Doane:\n"
    #     f"---------------------\n"
    #     f"Winner: {winner}\n"
    # )