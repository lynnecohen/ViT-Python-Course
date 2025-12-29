# ITP Week 3 Day 2 Exercise

# import in the two modules for making API calls and parsing the data

import json
import requests

# set a url variable to "https://rickandmortyapi.com/api/character"

url = "https://rickandmortyapi.com/api/character"

# set a variable response to the "get" request of the url

response = requests.get(url)

# print to verify we have a status code of 200

print(response)

# assign a variable json_data to the responses' json

json_data = response.json() # this converts the api info into a python dictionary

#  automatically converts JSON into Python objects.
# No need to use json.loads manually here

# print to verify a crazy body of strings!

print(json_data)
print("json_data type is", type(json_data))


# print the newly created python object
