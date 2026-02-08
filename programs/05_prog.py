# finding the missing number in a sequence

seq = [1, 2, 3, 4, 5, 7, 8]
n = 8

exp_sum = n * (n+1) // 2
actual_sum = sum(seq)

print('exp: ', exp_sum)
print('act', actual_sum)
print(exp_sum - actual_sum)