# write Palindrome program
str = input("Enter a string: ").strip().replace(" ", "").lower()

# Using s[::-1] (Built-in Function)
if(str == str[::-1]):
    print("It is a palindrome string.")
else:
    print("It is not a plaindrome string.")

# Using reversed() (Built-in Function)
# if str == "".join(reversed(str)):
#     print("It is a palindrome string.")
# else:
#     print("It is not a plaindrome string.")


#Ignore Spaces & Special Characters
# str = input("Enter a string: ").lower()

# clean = ""
# for s in str:
#     if s.isalnum():
#         clean += s

# if clean == clean[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
