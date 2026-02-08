#find second largest number from the list
list1 = [91, 2, 13, 14, 51]

largest = 0
second_largest = 0

for num in list1:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print('largest', largest)
print('2nd: ', second_largest)