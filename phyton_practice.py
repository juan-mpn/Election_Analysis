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

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# print("\nCounties----")
# for county in counties_dict.keys():
#     print(county)
# print("\nVoters===")
# for voters in counties_dict.values():
#     print(voters)
# print("\nCounties---- key")
# for county in counties_dict:
#     print(counties_dict[county])
# print("\nCounties---- get")
# for county in counties_dict:
#     # print(county)
#     print(county, counties_dict.get(county))

# print("\nCounties---- items")
# for key, value in counties_dict.items():
#     print(key, " has ", value," registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)
# print("\nVoting data === List using range")
# for i in range(len(voting_data)):
#     print(voting_data[i])

# print("\nNested loop=== using Values")
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)


# print("\nNested loop=== using items")
# for county_dict in voting_data:
#     for key, value in county_dict.items():
#         print(value)

print("\n loop=== registered voters = list")
for county_dict in voting_data:
#    print(county_dict['registered_voters'])
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")
        
# print("\n loop=== counties")
# for county_dict in voting_data:
#     print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))

# print("\nRegular Print")
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# print("\nPrint Formatted")
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

print("\n Counties === sample")
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    # print(county + " county has " + str(voters) + " registered voters.")
    print(f"{county} county has {voters} registered voters.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# # :{10}.{2}
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# print("\n", message_to_candidate,"\n")
