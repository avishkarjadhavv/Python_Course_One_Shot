# syntax for dictionary in Python is as follows:

# my_dict = {
#     'key1': 'value1',
#     'key2': 'value2',
# }

# syntax for accessing values in a dictionary:

# print(my_dict['key1'])  # Output: value1
# print(my_dict['key2'])  # Output: value2

a = {
    "Harry" : 100,
    "AJ" : 130 ,
    "list" : [2,6,4],
    "hello" : "world",
}

print(a["Harry"])  # Output: 100
print(a["AJ"])     # Output: 130
print(a["list"])   # Output: [2, 6, 4]
print(a["hello"])  # Output: world

print(a.get("Harry"))  # Output: 100
print(a.get("AJ"))     # Output: 130
print(a.get("list"))   # Output: [2, 6, 4]
print(a.get("hello"))  # Output: world

# difference between accessing values using square brackets and the get() method is that if the key does not exist, using square brackets will raise a KeyError, while get() will return None (or a default value if provided).

# example
print(a["not_exist_key"])  # This will raise a KeyError
print(a.get("not_exist_key"))  # None