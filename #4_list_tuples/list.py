a = ["alice" , 324 , 534.354 , True , False , 'A']

print("a[0] =",a[0])  # alice
print("a[1] =",a[1])  # 324

a[0] = 134 # changing the value of the first element
print("a[0] =",a[0])  # 134


# list slicing is a technique used to extract a portion of a list by specifying a start index and an end index. The syntax for slicing is: list[start_index:end_index]

print(a[1:4])  # [324, 534.354, True]
print(a[2:5])  # [534.354, True, False]
print(a[2:5:2])  # [534.354, False] this means that we are taking every second element from index 2 to index 5 (not including index 5)

print(a[4:2])  # [] this means that we are trying to slice from index 4 to index 2, which is not possible, so it returns an empty list

print(a[4:2:-1])  # [False, True] this means that we are slicing from index 4 to index 2 in reverse order, so it returns the elements at index 4 and index 3