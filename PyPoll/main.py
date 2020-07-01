# import modules
import os
import csv

# Get file path
csvpath = os.path.join("Resources","election_data.csv") # actual data csv
#csvpath = os.path.join("Resources","test.csv") # test csv of a sample from actual data

# Open csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header[2]}")

    # make lists to store candidate name and how many votes each one gets
    # start each list with data from row after header
    candidate = [next(csvreader)[2]]
    votes = [1]

    # Read each row of data after the second row
    for row in csvreader:
        if any(cand == row[2] for cand in candidate): # if candidate is already in list
            i = candidate.index(row[2]) # store index of candidate from the candidate list
        else: # otherwise add candidate to list and new vote tally entry in votes list
            candidate += [row[2]]
            votes += [0]
            i = len(candidate)-1 # again store index of the newly added candidate
        votes[i] += 1 # add one more vote to the candidate based off the selected index

total = sum(votes) # total number of votes

# print all results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total}")
print("--------------------------")
for x in range(len(candidate)):
    print(f"{candidate[x]}: {(votes[x]/total * 100):.3f}% ({votes[x]})")
print("--------------------------")
print(f"Winner: {candidate[votes.index(max(votes))]}")
print("--------------------------")

# store files in Analysis.txt file
f = open("Analysis.txt","w+")
print("Election Results",file=f)
print("--------------------------",file=f)
print(f"Total Votes: {total}",file=f)
print("--------------------------",file=f)
for x in range(len(candidate)):
    print(f"{candidate[x]}: {(votes[x]/total * 100):.3f}% ({votes[x]})",file=f)
print("--------------------------",file=f)
print(f"Winner: {candidate[votes.index(max(votes))]}",file=f)
print("--------------------------",file=f)