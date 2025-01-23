
# name = input ("Enter your full name: ")
# phone_number = input("Enter your phone number # : ")

# result = len(name) "Finds the length of the string (including space)"
# result = name.find(" ") "Finds the place of the specific character in the string starting from the beginning of the string (starts counting from 0)"
# result = name.rfind (" ") "Same as find method but in this case in will search for the character from the end on the string"
# name = name.capitalize () "Capitalize the first letter"
# name = name.upper() "Makes the the entire string upper case"
# name = name.lower() "Makes the entire string lower case"
# result = name.isdigit() "Will return True or False. True only if string only contains numbers"
# result = name.isalpha() "Will return True or False. True only if string contains only letters (NO SPACE)"
# result = phone_number.count("-") "Will return an integer. Will count how many specified character are within a string"
# result = phone_number.replace("-", "") "Replaces one occurrence of the character with another"

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain space")
elif not username.isalpha():
    print("Your username can't contain number")
else:
    print(f"Welcome {username}")