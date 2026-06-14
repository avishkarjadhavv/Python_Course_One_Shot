name = "Avishkar"

# here index of "A" is 0 and -8
# here index of "v" is 1 and -7
# here index of "i" is 2 and -6

# to access a character in a string we can use indexing

# syntax: string_name[start_index : end_index]

nameshort = name[0:5]  # output: "Avish"
print(nameshort)

print(name[0:4])  # output: "Avis"
print(name[-8:-4])  # output: "Avis"         NEGATIVE INDEXING


print(name[2:5])  # output: "ish"

print(len(name))  # output: 8  ---> length of the string


print(name[:])   # output: "Avishkar"  --->is same as name[0:8] or name[0:len(name)]
print(name[0:])  # output: "Avishkar"  ---> is same as name[0:8] or name[0:len(name)]
print(name[:8])  # output: "Avishkar"  ---> is same as name[0:8] or name[0:len(name)]



# now let's see some more types of string slicing

print(name[1:6:2])  # output: "vsk"     ---> it will print characters from index 1 to 6 with a step of 2

str = "abcdefghijklmnopqrstuvwxyz"

print(str[1:26:3])  # output: "behknqtwz"  ---> it will print characters from index 1 to 26 with a step of 3