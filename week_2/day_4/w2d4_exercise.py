# ITP Week 2 Day 4 Exercise

# 1. Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 0
}

for i in inventory:
    print(i, inventory[i])

# SCENARIO: A person came in and bought one of everything!

# for item in inventory:
    # decrement item by using an assignment operator

    # NOTE: recall that item represents the key of the key:value pair
def buyOneOfEverthing():
    for i in inventory:
        if(inventory[i] > 0):
            inventory[i] -= 1
            print(f"one {i} has been sold; there are {inventory[i]} remaining.")
        else: 
            print(f"sorry, we are fresh out of {i}.")

buyOneOfEverthing()

for i in inventory:
    print(i, inventory[i])

print("\n\n")

# 2. Implicit Functions 
# (When we work with global variables/objects and don't return anything, 
# these functions are implicit return functions!)

    # a. Dictionaries - create a function that takes in a dictionary which updates the "role" key value pair and makes it uppercase

user_1 = {
    "firstName": "Stephanie",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "95485"
}

user_2 = {
    "firstName": "Brion",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "67344"
}

user_3 = {
    "firstName": "Daniel",
    "lastName": "Kim",
    "role": "Instructor",
    "id": "74324"
}

instructor_list = [user_1, user_2, user_3]

print("\n Current Instructors Include:",instructor_list)

def roleUpper(dict):
    if(dict["role"]):
        dict["role"] = dict["role"].upper()

    # b. Dictionaries - Run the functions (3 times for each user!)

for instructor in instructor_list:
    roleUpper(instructor)
# print(instructor_list)

print("\n Updated Instructors Include:",instructor_list)

    # c. List - create a function that takes in the list and 
    # checks if the each user's role is equal to "INSTRUCTOR". 
    # if it is the same, print VALID else print INVALID (try to use a loop here!)

def role_check(list):
    for dict in list: 
        if(dict["role"] and dict["firstName"] and dict["lastName"]):
            if(dict["role"] == "INSTRUCTOR"):
                print("\n",dict["firstName"],dict["lastName"],"is a valid",dict["role"])
            else:
                print("\n",dict["firstName"],dict["lastName"],"is invalid. They are a/n",dict["role"])
        else: 
            print("\n","user is missing information: ",dict)

role_check(instructor_list)

    # d. import the random module and update the function to re-assign the id of each user

import random

def randomize_id(list):
    for dict in list:
        if(dict["id"]):
            dict["id"] = random.randint(10000,99999)
            print("\n",dict["firstName"],dict["lastName"],"has a new id:",dict["id"])
        else:
            print("\n","user is is missing.")

    # e. don't forget to run it!
randomize_id(instructor_list)
    
# 3. Explicit Functions
user_info = [46453, "Devin", "Smith"]
    # Each element by index of user_info follows the format of: id, first_name, last_name


    # Create a function with a parameter user_list
    #   - return a dictionary with the follow key value pairs:
    #   - id: user_list[0]
    #   - first_name: user_list[1]
    #   - last_name: user_list[2]

def createDict(user_list):
    user_dict = {
        "id": user_list[0],
        "first_name": user_list[1],
        "last_name": user_list[2]
    }
    return user_dict
