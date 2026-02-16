# finding duplicate (same) numbers in a list.
numbers = [6, 1, 2, 3, 4, 2, 5, 3, 6]

#Efficient Way
# duplicate = set()
# seen = set() 
# for n in numbers:
#     if n in seen:
#         duplicate.add(n)
#     else:
#         seen.add(n) 
# print("duplicate", duplicate) 

#Find Duplicate (Similar) Numbers
duplicate = []
for n in numbers:
    if numbers.count(n) > 1 and n not in duplicate:
        duplicate.append(n)
print(duplicate)
