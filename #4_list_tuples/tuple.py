a = (5, 10, 15 , 20, 25, 30)

print(type(a))  # <class 'tuple'>

b = () # empty tuple

d = (1)
print(type(d))  # <class 'int'> this is not a tuple, it is an integer

c = (1,) # tuple with one element, note the comma after the element is necessary to indicate that it is a tuple

print(type(c))  # <class 'tuple'>


# to access the elements of a tuple, we can use indexing and slicing just like we do with lists. The syntax for indexing is: tuple[index] and the syntax for slicing is: tuple[start_index:end_index]

print(a[0])  # access the first element