# ITP Week 1 Day 4 Exercise

# EASY

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1. loop through the lowercase and print each element

for letter in lowercase:
    print (letter)

# 2. loop through the lowercase and print the capitalization of each element

i = 0
while i < len(lowercase):
     print (lowercase[i].upper())
     i += 1
    
print (lowercase)
# we learned that for changing the items, the while loop works better than the for loop. 

# MEDIUM

# 1. create a new variable called uppercase with an empty list

uppercase = []

# 2. loop through the lowercase list
    # 2a. append the capitalization of each element to the uppercase list

for letter in lowercase:
    uppercase.append(letter.upper())

print(uppercase)
# HARD

# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.

password = "MySuperSafePassword!@34"

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# 1. create the following variables and assign them Booleans as False
    # has_uppercase
    # has_lowercase
    # has_number
    # has_special_char

has_uppercase = False
has_lowercase = False
has_number = False
has_special_char = False

# 2. loop through the string password (same as a list)
# OR you can create a new list variable of the string password
# using list(string) NOTE: assign it a new variable as such:
# password_list = list(password) prior to looping.

# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.

# NOTE: to see if it has a number, use range from 0 - 10!

numbers = list(range(10))
numbers = [str(x) for x in numbers]

print(numbers)

for char in password:
    if char in uppercase:
    # if char.isupper():
         has_uppercase = True
         print(f"char {char} is uppercase.")
    elif char in lowercase:
        has_lowercase = True
        print(f"char {char} is lowercase.")
    elif char in special_char:
        has_special_char = True
        print(f"char {char} is a designated special character.")
    elif char in numbers:
        has_number = True
        print(f"char {char} is a digit.")
    else:
        print(f"char {char} matches none of the above.")

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)

final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True

# NOTE: we can shorthand this by just checking if the variable exists (returns True)
#final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
# this will fail the same if any one of them is False

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop

if final_result:
    print ("SAFE STRONG PASSWORD")
else:
    print ("Update password: too weak")

# BONUS: update the password variable to take in an user input!

user_test = True

while user_test: 

    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special_char = False
    final_result = False

    print("\n\n A strong password has at least one uppercase character, one lowercase character, one number, and one special character such as ! @ # $ % ^ & ( ) *.")
    user_password = input("\n Enter a password to check its strength: ")

    for char in user_password:
        if char in uppercase:
            has_uppercase = True
            #print(f"char {char} is uppercase.")
        elif char in lowercase:
            has_lowercase = True
            #print(f"char {char} is lowercase.")
        elif char in special_char:
            has_special_char = True
            #print(f"char {char} is a designated special character.")
        elif char in numbers:
            has_number = True
            #print(f"char {char} is a digit.")
        #else:
            #print(f"char {char} matches none of the above.")

    # NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!
    final_result = has_uppercase and has_lowercase and has_number and has_special_char
    error_message = "Update password: too weak. "

    if not(has_uppercase):
        error_message += "Missing uppercase character. "
    if not(has_lowercase):
        error_message += "Missing lowercase character. "
    if not(has_special_char):
        error_message += "Missing special character. "
    if not(has_number):
        error_message += "Missing number. "

    if final_result:
        print ("SAFE STRONG PASSWORD")
    else:
        print (error_message)

    try_again = ""
    while try_again != "y" and try_again != "n":
        try_again = input("Would you like to try again? y/n: ")

    if try_again=="y":
        user_test = True
    else:
        user_test = False
    
