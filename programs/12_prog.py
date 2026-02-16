# #Retrieve Pairs Whose Sum = Target
# numbers = [2, 4, 3, 5, 7, 8]
# target = 12

# result = []

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             result.append((numbers[i], numbers[j]))
# print(result)

numbers = [2, 4, 3, 5, 7, 8]
target = 10

seen = set()
pairs = []

for num in numbers:
    complement = target - num
    if complement in seen:
        print("pairs:", pairs) 
        pairs.append((complement, num))
    seen.add(num)
    print("seen:", seen) 

print("Interaction pairs:", pairs) 