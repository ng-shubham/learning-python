#Problem: Sort Bug Frequencies

n = int(input("Enter number of bugs: "))
bugs = list(map(int, input("Enter bug IDs separated by space: ").split()))

freq = {}

for bug in bugs:
    if bug in freq:
        freq[bug] += 1
    else:
        freq[bug] = 1

sorted_bugs = sorted(freq.items(), key=lambda x: x[1], reverse = True)

for i, j in sorted_bugs:
    print(i, j)
 
# input: 
# Enter number of bugs: 10
# Enter bug IDs separated by space: 5 2 4 1 1 5 2 5 1 5

# output:
# 5 4
# 1 3
# 2 2
# 4 1
