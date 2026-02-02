s1 = {1, 2, 3, 8, 9}
s2 = {3, 4, 5, 1, 7}
# Union
print(s1 | s2)  # Output: {1, 2, 3, 4, 5, 7, 8, 9}
# Intersection
print(s1 & s2)  # Output: {1, 3}
# Difference
print(s1 - s2)  # Output: {2, 8, 9} explanation: elements in s1 not in s2
print(s2 - s1)  # Output: {4, 5, 7} explanation: elements in s2 not in s1
# Symmetric Difference
print(s1 ^ s2)  # Output: {2, 4, 5, 7, 8, 9}    explanation: elements in either s1 or s2 but not both   
# Using methods
print(s1.union(s2))               # Output: {1, 2, 3, 4, 5, 7, 8, 9}
print(s1.intersection(s2))        # Output: {1, 3}
print(s1.difference(s2))          # Output: {2, 8, 9} explanation: elements in s1 not in s2
print(s2.difference(s1))          # Output: {4, 5, 7} explanation: elements in s2 not in s1
print(s1.symmetric_difference(s2))# Output: {2, 4, 5, 7, 8, 9} explanation: elements in either s1 or s2 but not both
# In-place operations
s1 |= s2    # union, explained: adds elements of s2 to s1
print(s1)  # Output: {1, 2, 3, 4, 5, 7, 8, 9}
s1 &= s2  # intersection, explained: keeps only elements also in s2
print(s1)  # Output: {1, 3}
s1 -= s2  # difference, explained: removes elements of s2 from s1
print(s1)  # Output: set()
s1 ^= s2  # symmetric difference, explained: elements in either s1 or s2 but not both
print(s1)  # Output: {3, 4, 5, 1, 7}