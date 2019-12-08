# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
# if  percentage_votes > 50.1:
#    print("\nWinner !!!!\n")
# else:
#    print("You are not the Winner")

# # =========================== 
# print("Counties\n")
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# if counties[2] != 'Jefferson':
#    print(counties[2])

# print("Temperature\n")
# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.\n")
# else:
#     print("Open the windows.\n")
    
# #What is the score?
# score = int(input("What is your test score? "))

# Determine the grade.
# # What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

for county in counties:
    print(county)
    