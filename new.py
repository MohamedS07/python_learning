# import json

# employee = '{"name": "Alex","age": 25,"isStudent": true,"skills": ["Python","SQL"],"address": { "city":"Mumbai","pincode": 400001}}'

# a = json.loads(employee)
# print(a)

# print(a["address"]["city"])
# print(a["skills"][1])


# emp = {"name": "Alex","age": 25,"isStudent": True,"skills": ["Python","SQL"],"address": { "city":"Mumbai","pincode": 400001}}

# b = json.dumps(emp)
# print(b)
# print(type(b))

import json
import requests

response = requests.get("https://randomuser.me/api/")
data = response.json()
user = data["results"][0]
name = user["name"]["first"]
email = user["email"]
city = user["location"]["city"]
print("Name:", name)
print("Email:", email)
print("City:", city)






