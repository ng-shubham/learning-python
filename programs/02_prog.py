# write count occurrences in the string
name = "Hey, how are you doing?"

# using count function
# count = name.count("o")
# print(count)

# using for loop
l = 'o'
count = 0
for letter in name:
    if letter == l:
        count += 1

print(count)