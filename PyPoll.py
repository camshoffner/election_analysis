# Data that is needed for this project:
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

#Assign a variable for the file to load 
import csv
import os

#File to load - Election results
file_to_load = os.path.join("Resources", "election_results.csv")

#File to Save 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use With statement to open / close file
with open(file_to_load, "r") as election_data:

    # To do : read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Store and print header row
    headers = next(file_reader)
    print(headers)

    # Print each row in teh CSV file.
  #  for row in file_reader:
  #      print(row)
    #Write data to file
#    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")