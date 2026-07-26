s = set()

s.add(20)
s.add(float(20.0))          # here 20.0 = 20 , so no repeating values of 20
s.add("20")

print(s,len(s))