# ITP Week 3 Day 1 Exercise

# ENUMERATE!

# 1. Read all instructions first!
# 
# Prompt: given a list of names, create a list of dictionaries with the index as the user_id and name

users_list = ["Alex", "Bob", "Charlie", "Dexter", "Edgar", "Frank", "Gary"]

# example output    
# [{"user_id": 0, "name": "Alex"}, etc, etc]

# 1a. Create a function that takes a single string value and returns the desired dictionary

def name_to_dict(index, name):
        new_dict = {
            "user_id": index,
            "name": name
        }
        return(new_dict)

# 1b. Create a new empty list called users_dict_list

users_dict_list = []

# 1c. Loop through users_list that calls the function for each item and appends the return value to users_dict_list

for index, value in enumerate(users_list):
       newdict = name_to_dict(index, value)
       users_dict_list.append(newdict)

print("\n\n Users Dict List: ",users_dict_list)

# 2. Prompt: Given a series of dictionaries and desired output (mock_data.py), can you provide the correct commands?
from mock_data import mock_data
# 2a. retrieve the gender of Morty Smith

# print("\n\n", mock_data)

for index, value in mock_data.items(): #loop through the dictionaries contained in the dictionary "mock data"

    if index == "results": # locate the index value "results", which is a LIST of DICTIONARIES
        # print("\n\nfound results list: ")
        for dict in value: # loop through the list of dictionaries
            # print("\n",dict)
            if dict["name"] == "Morty Smith":
                print(f"\nMorty's gender is {dict['gender']}.")
            # else:
            #     print("\nThis is",dict["name"],"not Morty.")

# 2b. retrieve the length of the Rick Sanchez episodes
        for dict in value: 
            if dict["name"] == "Rick Sanchez":
                 episodelist = dict["episode"]
                 print("\nThere are",len(episodelist),"episodes featuring Rick Sanchez.")

# 2c. retrieve the url of Summer Smith location
        for dict in value:
             if dict["name"] == "Summer Smith":
                  location_dict = dict["location"]
                  
                  print(f"\nSummer is currently at the location {location_dict['name']}, url {location_dict['url']}.")

print("\n\n")