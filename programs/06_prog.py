# from collections import Counter

# str = input("Enter a string: ").strip()

# freq = Counter(str)

# for i, j in freq.items():
#     print(i, j)

str = input("Enter string: ").strip()
freq = {}

for s in str:
    if s in freq:
        freq[s] += 1 
    else:
        freq[s] = 1

for key in freq:
    print(key, freq[key])