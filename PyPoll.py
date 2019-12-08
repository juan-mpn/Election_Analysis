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