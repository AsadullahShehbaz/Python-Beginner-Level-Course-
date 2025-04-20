obj = {
    "name":"Faheem",
    "Age ": 19,
    "Section":"Pasha",
    "City":"Payathaht",
    "list":[11,12,13]
}

print(obj.items()) 
# to get the key value pair
print(obj.keys())
 # to get the key only 
# print(type(obj))
#  to get the type of the variable
print(obj.get("City")) 
# get method to get the value at a specific key
obj.update({"name":"Sultan Abdul Majeed","Class":1909})
#update method to update the value at a specific key 
print(obj.get("name"))
print(obj["name"])