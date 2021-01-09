import pathlib
import csv

csvpath = pathlib.Path("data/election_data.csv")
# print(csvpath)

# creates blank lists for data to be added into
votes = []
candidate_votes = []

with open(csvpath, mode = "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)

    for row in reader:
        votes.append(row[0])
        candidate_votes.append(row[2])

# begins the process to print results to txt
f = open("results.txt", "w")

# TOTAL VOTES
# total number of votes equals the length of the list that includes the voter IDs
total_votes = len(votes)

# CANDIDATE LIST
# using a function to find if current value in candidate list is a duplicate or not

candidate_list = []
for name in candidate_votes:
    if name not in candidate_list:
        candidate_list.append(name)
# print(candidate_list)

number_of_candidates = len(candidate_list)    
# print(number_of_candidates)

vote_counts = []
for i in range(0, number_of_candidates):
    # vote_counts = []
    vote_sum = sum(1 for x in candidate_votes if x == candidate_list[i])
    vote_counts.append(vote_sum)
# print(vote_counts)

percents = []
for i in range(0, number_of_candidates):
    vote_percentage = round((vote_counts[i] / total_votes) * 100, 2)
    percents.append(vote_percentage)
# print(percents)

def output_votes(): 
    for i in range(0, number_of_candidates):
        print(f"{candidate_list[i]}: {percents[i]}% ({vote_counts[i]})", file=f)

def winner_output():
    winner_percent = max(percents)
    winner_index = percents.index(winner_percent)
    print(f"Winner: {candidate_list[winner_index]}", file=f)

# test: print(winner_percent)

# #OUTPUT RESULTS

print(f"Election Results", file=f)
print(f"------------------------------", file=f)
print(f"Total Votes: {total_votes}", file=f)
print(f"------------------------------", file=f)
output_votes()
print(f"------------------------------", file=f)
winner_output()
print(f"------------------------------", file=f)

f.close()