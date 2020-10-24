import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
cand_dict={}

#The total number of votes cast
# Method 1: Plain Reading of CSV files
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next (reader, None)
    for row in reader:
        #make sure row count doesn't include the header
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in cand_dict:
            cand_dict [candidate_name] = 1
        else:
            cand_dict [candidate_name] +=1
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
mytext = "Election Results\n"
mytext += "--------------------------\n"
mytext += f"Total Votes: {total_votes}\n"
mytext += "--------------------------\n"
mysort = sorted(cand_dict.items(), key = lambda x: x[1], reverse = True)
mywinner = mysort[0][0]
for i in mysort:
    cand = i[0]
    vote = i[1]
    per_votes = 100*vote/total_votes
    mytext += f"{cand}: {per_votes:.3f}% ({vote})\n"
mytext += "--------------------------\n"
mytext += f"Winner: {mywinner}\n"
mytext += "--------------------------\n"
print (mytext)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#'w' open file and write to it
textpath = os.path.join('Analysis', 'Election_Data.txt')
with open (textpath,"w") as txtfile:
    txtfile.write (mytext)


