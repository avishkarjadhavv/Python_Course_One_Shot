s = { 1 ,4 ,2 }
print(type(s))  # Output: <class 'set'>

print(s)  # Output: {1, 2, 4}

#empty set

e1 = set()
print(type(e1))  # Output: <class 'set'>

e2 = {}
print(type(e2))  # Output: <class 'dict'>

# so don't use {} to create an empty set it will create a empty dictionary , use set() instead.



# set doesn't allow duplicate values , repeated values will be ignored and only unique values will be stored in the set.

r = {3 ,5 ,4 ,5, 7,4, 3, 2,2,2,4}
print(r) # Output: {2, 3, 4, 5, 7}