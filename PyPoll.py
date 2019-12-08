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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

        # Print each row in the CSV file.
    lines = 10
    # Print the header row.
    headers = next(file_reader)
    for row in file_reader:
        print(row[0])
        lines -= 1
        if lines < 1:
            break
    print(f"\nHeaders\n{headers}")
