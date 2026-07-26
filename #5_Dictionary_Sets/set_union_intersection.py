s1 = { 1 , 2 , 3 , 4 }

s2 = { 6 , 7 , 4 ,2 }

# union() method is used to combine two sets. It returns a new set that contains all the elements from both sets, without duplicates.
s3 = s1.union(s2)
print(s3) # Output: {1, 2, 3, 4, 6, 7}

# intersection() method is used to find the common elements between two sets. It returns a new set that contains only the elements that are present in both sets.

s4 = s1.intersection(s2)
print(s4) # Output: {2, 4}



print(s1-s2)  # removes those elements from s1 which are present in s2    output :- {1,3}


# issuperset() method

print(s1.issuperset({1,3}))    # output :- True


#issubset method

print({1,3}.issubset(s1))   # output :- True