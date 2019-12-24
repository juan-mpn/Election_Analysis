# Election_Analysis
## Author
Juan M. Pacheco
12/8/2019
UCB Data Analytics
Python, VS Studio
## Project Overview
A Colorado Board of Election employee has given us the following tasks to complete the election audit of a recent local congressional election. 

## Pseudo Code
1. Open the data file.
2. Write down the names of all the candidates.
3. Add a vote count for each candidate.
4. Get the total votes for each candidate.
5. Get the total votes cast for the election.

1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candicate won
5. the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- software: Python 3.6.1 Visual Studio Code, 1.38.1

## Summary
Total number of votes cast
A complete list of candidates who received votes
Total number of votes each candidate received
Percentage of votes each candidate won
The Candidates were:
- Candidate 1
- Candidate 2
- Candidate 3
The Candidates results were: 
- Candidate 1 received "x%" of the vote and "y" number of votes.
- Candidate 2 received "x%" of the vote and "y" number of votes.
- Candidate 3 received "x%" of the vote and "y" number of votes.
The winner of the election based on popular vote
- Candidate (1,2 or 3) who received "x%" of the vote and "y" number of votes.

## Challenge Overview
The goals of this challenge are for you to:

Extend your use of for loops and conditionals with membership and logical operators.
Scope and refactor code to provide additional information.
Write data to an output file and print the file.
ie. 
-------------------------
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
-------------------------
Largest County Turnout: Denver
-------------------------

## Challenge Summary
Make a copy of the PyPoll.py file that you used throughout this module and rename it PyPoll_Challenge.py.
Create a list for the counties.
Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
Create an empty string that will hold the county name that had the largest turnout.
Declare a variable that represents the number of votes that a county received. Hint: Inside a for loop, add an if statement to check if the county name has already been recorded. If not, add it to the list of county names.
Inside the with open() function where you are outputting the file, do the following:
Create three if statements to print out the voter turnout results similar to the results shown above.
Add the results to the output file.
Print the results to the command line.
