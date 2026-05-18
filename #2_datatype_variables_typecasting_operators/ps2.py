# add two numbers

a = 12
b = 3
print("Addition of",a,"and",b,"is",a+b)

# divide by n , find remainder                div = divisor * q + r

num = int(input("Enter value of num :"))
n = int(input("Enter a number to divide with num :"))

divisor = int(num/n)

r = num - (divisor*n)     # ------> just use r = num % n  <-------

print("The remainder is",r,"after dividing",num,"with",n)

# comparision operator

g = int(input("Enter the value of g : "))
h = int(input("Enter the value of h : "))

print(g,"is greater than",h,":",g>h)


# average and square of input numbers

i = float(input("Enter the value of i : "))
j = float(input("Enter the value of j : "))

print("Average of",i,"and",j,"is",(i+j)/2)
print("Sqaure of",i,"is :",i*i)