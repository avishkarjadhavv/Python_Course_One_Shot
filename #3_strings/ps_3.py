#display a user entered name followed by a welcome message using input() function

name1 = input("Enter your name :")

print("Welcome",name1,"Good to see you here")


# question no . 2

letter = '''Dear <|name|>,
You are selected in our company.
<|Date|>'''

name2 = input("Enter your name :")
date = input("Enter date of selection :")

letter = letter.replace("<|name|>",name2)
letter = letter.replace("<|Date|>",date)
print(letter)


#write a program to detect double spaces in a string

str = "This is a string with double  spaces."
print(str.find("  "))  # output: 24  ---> it will return the index of the first occurrence of double spaces in the string

# replace double spaces with single space

print(str.replace("  "," "))  # output: "This is a string with double spaces."  ---> it will replace double spaces with single space


#format this string using escape sequence

letter2 = "Dear Harry,This python course is nice.Thanks!"

letter3 = "Dear Harry,\n\tThis python course is nice.\n\tThanks!"
print(letter3)