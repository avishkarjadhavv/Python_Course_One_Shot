# write a program to store 7 fruits from user in a list and print them without using for loop

fruits = [] # creating an empty list to store the fruits

print("Enter the names of 7 fruits :")

a = input("Fruit 1 = :") # taking input from the user for the first fruit
fruits.insert(0,a) # inserting the first fruit at index 0

b = input("Fruit 2 = :") # taking input from the user for the second fruit
fruits.insert(1,b) # inserting the second fruit at index 1

c = input("Fruit 3 = :") # taking input from the user for the third fruit
fruits.insert(2,c) # inserting the third fruit at index 2

d = input("Fruit 4 = :") # taking input from the user for the fourth fruit
fruits.insert(3,d) # inserting the fourth fruit at index 3

e = input("Fruit 5 = :") # taking input from the user for the fifth fruit
fruits.insert(4,e) # inserting the fifth fruit at index 4

f = input("Fruit 6 = :") # taking input from the user for the sixth fruit
fruits.insert(5,f) # inserting the sixth fruit at index 5

g = input("Fruit 7 = :") # taking input from the user for the seventh fruit
fruits.insert(6,g) # inserting the seventh fruit at index 6

print("The fruits you entered are:")
print(fruits)