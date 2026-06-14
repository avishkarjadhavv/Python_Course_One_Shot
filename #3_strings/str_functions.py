str = "harRy bhAi"

print(len(str))  # output: 11  ---> length of the string

print(str.upper())  # output: "HARRY BHAI"  ---> it will convert all characters to uppercase

print(str.lower())  # output: "harry bhai"  ---> it will convert all characters to lowercase

print(str.capitalize())  # output: "Harry bhai"  ---> it will convert the first character to uppercase and the rest to lowercase

print(str.title())  # output: "Harry Bhai"  ---> it will convert the first character of each word to uppercase


print(str.replace("bhAi" , "bhau"))  # output: "harRy bhau"  ---> it will replace the substring "bhai" with "bhau"


print(str.find("bhA"))  # output: 6  ---> it will return the index of the first occurrence of the substring "bhA" in the string

print(str.endswith("Ai"))  # output: True  ---> it will return True if the string ends with the substring "Ai" else it will return False

print(str.startswith("har"))  # output: True  ---> it will return True if the string starts with the substring "har" else it will return False
