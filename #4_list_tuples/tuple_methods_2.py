# concatenate tuples

t1 = (3 , 4 , 7)
t2 = (8 , 2 , 5)

t3 = t1 + t2 # this will concatenate the two tuples and create a new tuple
print(t3)  # (3, 4, 7, 8, 2, 5)


# Repeating tuples

t4 = t1 * 3 # this will repeat the tuple t1 three times and create a new tuple
print(t4)  # (3, 4, 7, 3, 4, 7, 3, 4, 7)


# in operator

print("4 exists in t1 :",4 in t1)  # this will return True because 4 is an element of the tuple t1
print("5 exists in t1 :",5 in t1)  # this will return False because 5 is not an element of the tuple t1


# min and max functions

print("Minimum value in t1 :",min(t1))  # this will return the minimum element of the tuple t1, which is 3
print("Maximum value in t1 :",max(t1))  # this will return the maximum element of the tuple t1, which is 7