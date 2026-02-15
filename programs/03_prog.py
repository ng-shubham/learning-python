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
