#frequency-count program
from collections import Counter

str = input("Enter a string: ").strip()

freq = Counter(str)

for k,v in freq.items():
    print(k ,v)