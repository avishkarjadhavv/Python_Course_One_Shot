price = {
    "kia" : 200,
    "toyota" : 345,
    "Tata" : 100,
}


# items() method returns a list of tuples, where each tuple contains a key-value pair from the dictionary.

print(price.items())  # Output: dict_items([('kia', 200), ('toyota', 345), ('Tata', 100)])


#keys() method returns a list of all the keys in the dictionary.

print(price.keys())  # Output: dict_keys(['kia', 'toyota', 'Tata'])


#values() method returns a list of all the values in the dictionary.

print(price.values())  # Output: dict_values([200, 345, 100])


# update() method is used to update the dictionary with the elements from another dictionary object or from an iterable of key-value pairs.

price.update({"kia": 150 , "verna" : 230})

print(price)  # Output: {'kia': 150, 'toyota': 345, 'Tata': 100, 'verna': 230}
# kia gets updated to 150 and verna is added to the dictionary with a value of 230.



# get() method returns the value for the specified key if the key is in the dictionary. If not, it returns None (or a default value if provided).

print(price.get("kia"))  # Output: 150
print(price.get("AJ"))  # Output: None


# copy() method returns a shallow copy of the dictionary.
copy_dict = price.copy()
print(copy_dict)  # Output: {'kia': 150, 'toyota': 345, 'Tata': 100, 'verna': 230}