# Data that is needed for this project:
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

#Assign a variable for the file to load 
import csv
from functools import total_ordering
import os

#File to load - Election results
file_to_load = os.path.join("Resources", "election_results.csv")

#File to Save 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Variables
total_votes = 0 #intial vote counter
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Lists
candidate_options=[] #Stores all the candidates in the csv

#Dictionaries
candidate_votes = {} #Stores {Candidate name : votes}

#Use With statement to open / close file
with open(file_to_load, "r") as election_data:

    # To do : read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Store header row
    headers = next(file_reader)
    
    # Print each row in teh CSV file.
    for row in file_reader:
        total_votes+= 1 #tally all votes
        candidate_name = row[2] #Print candidate name for each row
        if candidate_name not in candidate_options: #Add to list if not in array already
          candidate_options.append(candidate_name)
          candidate_votes[candidate_name]=0

        #Tally votes for individual candidates
        candidate_votes[candidate_name]+= 1


    #print('total votes = ' + str(total_votes))
    #print(candidate_options)
    #print(candidate_votes)
    #calculate/ print percentages: vote_percentage = float(candidate_votes/total_votes)*100 
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes/total_votes)*100 
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
          winning_count = votes
          winning_percentage = vote_percentage
          winning_candidate = candidate_name
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
   # print(f"Congrats to {winning_candidate}! They received {winning_count:,} votes, which was {winning_percentage:.1f}% of the total votes casted" )
    #Calculating the Winner
    


    #Write data to file
  #  txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")