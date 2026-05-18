# + , - , * , /               Arithmetic operators
# = , += , -=                 Assignment operators
# == , <= , >= , < , > , !=   Comparison operators
# and or not                  Logical operators        


a = 12
b = 4

# print(a+b)

b+=3            # b+=3  ------->  b = b+3

# 3 ways to print sentence and variable in same line of code
# print("b =",b)
# print(f"b = {b}")              # f-string way
# print("b = " + str(b))        # string concatenation

# print("b =",b , "and what")    #just use comma for one same line code


# d = 5>6             # this will always print value in boolean
# print(d)

# e = 7<9
# print(e)


# --------------->  truth table for and

print("True and True is",True and True)
print("True and False is",True and False)
print("False and True is",False and True)
print("False and False is",False and False,"\n")

# --------------->  truth table for or

print("True or True is",True or True)
print("True or False is",True or False)
print("False or True is",False or True)
print("False or False is",False or False,"\n")


#not operator   -------> Interchange the boolean 

print(not(True))
print(not(False))