# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candicate won
# 5. the winner of the election based on popular vote

# Import the datetime dependency.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print(f"\nThe time right now is, {now}\n")


# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)

# # To do: perform analysis.

# # Close the file.
# election_data.close()


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# # outfile.close()

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# print("Open using ---- with")
# with open(file_to_save, "w") as txt_file:

#     # # Write some data to the file.
#     # txt_file.write("Hello World")

#          # Write three counties to the file.
#          txt_file.write("Countries in the Election\n")
#          txt_file.write("---------------------------\n")
#          txt_file.write("Arapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# declare candidate list 
candidate_options = []
# declare empty dictionary 
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Header row.
    headers = next(file_reader)

    # print only 10 lines
    lines = 10
    # Initializa Analysis variables
    total_votes = 0
    # Print each row in the CSV file.
    for row in file_reader:
#        print(row) # row[0])
#        lines -= 1
#        if lines < 1:
#            break
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] += 1

    # Print Header
    print(f"\nHeaders\n{headers}")
    # Print total votes
    print(f"\nTotal Votes: {total_votes}")
    # Print the candidate list.
    print(f"\nCandidate Options\n {candidate_options}\n")
    # Print the candidates dictionary
    print(f"\nCandidate Votes Dictionary\n {candidate_votes}\n")

    # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate}: received {vote_percentage:.1f}% of the vote.") 
# Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate  
print("\n-------------------------------------")
print("Winner Candidate!!!")
print("-------------------------------------")
print(f"Winning Candidate  Percent  Count")
print(f"{winning_candidate}       {winning_percentage:.1f}    {winning_count}\n")
