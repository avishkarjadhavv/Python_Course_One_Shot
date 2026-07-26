# add() method is used to add an element to the set.

s = { 1, 2 ,3 ,4}
s .add(67)
print(s)  # Output: {1, 2, 3, 4, 67}

# clear() method is used to remove all the elements from the set.
# copy() method returns a shallow copy of the set.

# both clear() and copy() methods are same as dictionary


# length of set
s1 = { 1, 2 ,6 ,5}
print(len(s1)) # Output: 4

# remove() method is used to remove an element from the set. If the element is not present in the set, it raises a KeyError.
s1.remove(6)
print(s1) # Output: {1, 2, 5}

