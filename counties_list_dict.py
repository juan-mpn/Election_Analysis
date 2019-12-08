# # List with Dictionaries {}
# print("List with Dictionaries=")
# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# print(voting_data)
# print("Add County=")
# voting_data.append({"county":"El Paso", "registered_voters": 461149})
# print(voting_data)
# voting_data.remove("Arapahoe")
# voting_data[2] = {"county":"Denver", "registered_voters": 463353}
# voting_data[1] = {"county":"Jefferson", "registered_voters": 432438}
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

# First, create an empty list called voting_data.

voting_data = []
# Then add, or append, each dictionary to the voting_data list with the following code and press Enter: 
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# When we type voting_data and press Enter, we get the following output:
voting_data.append({"county":"El Paso", "registered_voters": 461149})
# voting_data.remove(["Arapahoe"])
voting_data.pop(0)
print(f"\n\n\n\nThis is voting data: \n", voting_data)
voting_data
print(len(voting_data))
print(voting_data[0])
third = voting_data[0]
second = voting_data[1]
first = voting_data[2]
print("\n")
print(f"First",first)
print(f"Second", second)
print(f"Third",third)
voting_data.pop()
voting_data.pop()
voting_data.pop()
voting_data.append(first)
voting_data.append(second)
voting_data.append(third)
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(f"\nThis is voting data: \n", voting_data)
voting_data



