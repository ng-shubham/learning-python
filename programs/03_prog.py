# write Palindrome program

str = input("Enter a string: ").strip()

if(str == str[::-1]):
    print("It is a palindrome string.")
else:
    print("It is not a plaindrome string.")
