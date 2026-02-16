#string modification programs

# Replace Character at Specific Index
s = input("Enter a string: ")
index = int(input("Enter a index: "))
new_char = input("Enter a new charachter: ")

lt = list(s)
lt[index] = new_char

string = "".join(lt)
print(string)

# Replace All Occurrences of a Character
s = input("Enter a string: ")
old_str = input("Character to replace: ")
new_str = input("New Character: ")

final_str = s.replace(old_str, new_str)
print(final_str)


# Remove Special Characters
s = input("Enter a string: ")
result = ""
for i in s:
    if i.isalnum():
        result += i

print(result)

#Most Important for Interviews
# split()
# join()
# replace()
# strip()
# find()
# count()
# isalpha()
# isdigit()