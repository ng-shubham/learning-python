#frequency-count program

#using build-in function
# from collections import Counter
# str = input("Enter a string: ").strip()

# freq = Counter(str)
# for k,v in freq.items():
#     print(k ,v)


#without build-in function
# s = input("Enter a string: ").strip()
# freq = {}
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# for key, value in freq.items():
#     print(key, value)


# Word Frequency Program (Interview Favorite)
# Ignore case & Ignore punctuation & Sorted by frequency

# s = input("Enter string: ").strip().lower()
# words = s.split()
# freq={}

# for word in words:
#     clean_word = ""
#     # Remove non-alphabet characters manually
#     for ch in word: 
#         if ch.isalpha():
#             clean_word += ch

#     if clean_word:
#         if clean_word in freq:
#             freq[clean_word] += 1
#         else:
#             freq[clean_word] = 1

# # Sort by frequency
# sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse = True )

# for word, count in sorted_words:
#     print(word, count) 
