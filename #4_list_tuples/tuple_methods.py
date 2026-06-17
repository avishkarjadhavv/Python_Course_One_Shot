a = (6 ,3 ,8 ,2 ,"hello" , True , 2 , 1)
print(a)  # (6, 3, 8, 2, 'hello', True , 2, 1)

print(a.count(3))  # this will return the number of times the element 3 appears in the tuple, which is 1

print(a.index(2))  # this will return the index of the first occurrence of the element 2 in the tuple, which is 3, because the first occurrence of 2 is at index 3

print(a.index("hello"))  # this will return the index of the first occurrence of the element "hello" in the tuple, which is 5

print(a.index(True))  # this will return the index of the first occurrence of the element True in the tuple, which is 5, because in Python, True is considered as 1 and False is considered as 0, so it will return the index of the first occurrence of 1 in the tuple, which is 5

print(a.count("hello"))  # this will return the number of times the element "hello" appears in the tuple, which is 1

print(a.count(True))  # this will return the number of times the element True appears in the tuple, which is 1, because in Python, True is considered as 1 and False is considered as 0, so it will return the number of times 1 appears in the tuple, which is 2 , True is considered as 1 and it appears twice in the tuple, once as True and once as 1

print(len(a))  # this will return the number of elements in the tuple, which is 8