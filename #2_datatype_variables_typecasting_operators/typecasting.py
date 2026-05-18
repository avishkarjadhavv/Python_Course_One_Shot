a = 12
b = 42.43
c = "AJ"
d = 'a'
e = "13"

x = type(b)
y = type(c)
z = type(d)

print(type(a))
print(x)
print(y)
print(z)
print(type(e))        #   e is str ,not int

print(type(a+b))      #   int + float is float


# changing type of variable                ,  only if possible , can't convert str into int or float

h = 24.2
print("h = ",h)
h = int(h)
print("h = ",h)



g = "13.14"
print(type(g))

i = float(g)
print(type(i))