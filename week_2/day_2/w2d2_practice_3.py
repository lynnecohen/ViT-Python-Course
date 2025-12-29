# ITP Week 2 Day 2 (In-Class) Practice 3

# Functions Parameters and Arguments

# Lets take those functions we built in practice_2 and make them more dynamic:

x = 5
y = 7
# Rewrite the functions from practice_2 using parameters:
# add_num

def add_num(x, y):
    print(x + y)
    return(x + y)

add_num(x, y)

# subtract_num
def subtract_num(x, y):
    print(x - y)
    return(x - y)

subtract_num(x, y)

# multiply_num
def multiply_num(x, y):
    print (x * y)
    return(x * y)

multiply_num(x, y)

# divide_num
def divide_num(x, y):
    print(x / y)
    return(x/y)

divide_num(x, y)

# Don't forget to call your functions to make sure they work

#Uncomment to call your functions:
print("I should see the number 7 below from add_num: ")
add_num(3, 4)

print("I should see the number -2 below from subtract_num: ")
subtract_num(6, 8)

print("I should see the number 18 below from multiply_num: ")
multiply_num(2, 9)

print("I should see the number 2 below from divide_num: ")
divide_num(10, 5)

# Extra Time?

# Now take in 2 users inputs and pass them 
# in as arguments when calling the functions

print("\n\n")
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

print(f"{first_number} + {second_number} = {add_num(first_number, second_number)}")
print(f"{first_number} - {second_number} = {subtract_num(first_number, second_number)}")
print(f"{first_number} * {second_number} = {multiply_num(first_number, second_number)}")
print(f"{first_number} / {second_number} = {divide_num(first_number, second_number)}")
