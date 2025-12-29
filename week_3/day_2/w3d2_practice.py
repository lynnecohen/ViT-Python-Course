# ITP Week 3 Day 2 Practice

# 1. import the appropriate module

import json

# json examples:
# 
# from dummy_json import dummy_json  # pretend file with JSON text
# Convert JSON string into Python dictionary
# converted_json_dictionary = json.loads(dummy_json)
# print(converted_json_dictionary)
# print(converted_json_dictionary["researcher"]["relatives"][0]["name"])

json_1 = """
{
    "albumId": 1,
    "id": 1,
    "title": "accusamus beatae ad facilis cum similique qui sunt",
    "url": "https://via.placeholder.com/600/92c952",
    "thumbnailUrl": "https://via.placeholder.com/150/92c952"
}
"""

print("json_1 has the type",type(json_1))

# 2. perform a deserialization of the above object
python_1 = json.loads(json_1)

print("python_1 has the type",type(python_1))

# 3. assign a new variable called url_1 to the value of the deserialized object's url

url_1 = python_1["url"]
print("url_1 is", url_1)

json_2="""
[
{
"albumId": 1,
"id": 1,
"title": "accusamus beatae ad facilis cum similique qui sunt",
"url": "https://via.placeholder.com/600/92c952",
"thumbnailUrl": "https://via.placeholder.com/150/92c952"
},
{
"albumId": 1,
"id": 2,
"title": "reprehenderit est deserunt velit ipsam",
"url": "https://via.placeholder.com/600/771796",
"thumbnailUrl": "https://via.placeholder.com/150/771796"
}
]
"""

# 4. deserialize and assign a variable url_2 with the second item's url

python_2 = json.loads(json_2) # List of dictionaries


for i in python_2:
    python2_seconditem = python_2[1] # grab second dictionary
    url_2 = python2_seconditem["url"] # grab url from second dictionary

print("url_2 is", url_2)
