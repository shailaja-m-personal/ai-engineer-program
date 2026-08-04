#import ipython.display as display
#key-value pairs
#initialize dictionary
dict1 = {}
dict2 = {
            "name": "John", 
            "age": 30, 
            "city": "New York",
            "hobbies": ["reading", "traveling", "swimming"]
        }
print(type(dict2))
print(dict2)

#accessing values using keys
print(dict2["name"])

#modifying existing key-value pair
dict2["age"] = 31
print(dict2)

#adding new key-value pair
dict2["country"] = "USA"
print(dict2)

print(dict2['hobbies'],
        dict2.get('hobbies')[2])

print(dict2.keys())
print(dict2.values())
print(dict2.items())
print(dict2.pop('name'))
print(dict2)

print(dict2.pop('english', 'Key not present in dictionary')) #if key is not present, it returns the default value

dict2.update({"eye": "white"})
print(dict2)
print(dict2.popitem()) #removes last inserted key-value pair
print(dict2)