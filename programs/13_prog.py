# def generate_subsequence(s, index=0, current=""):
#     if index == len(s):
#         print(current)
#         return
    
#     # Include current character
#     generate_subsequence(s, index + 1, current + s[index])
    
#     # Exclude current character
#     generate_subsequence(s, index + 1, current)


# # Example
# generate_subsequence("abc")


def subsequence_k(s, k, index=0, current=""):
    if len(current) == k:
        print(current)
        return
    if index == len(s):
        return
    
    subsequence_k(s, k, index + 1, current + s[index])
    subsequence_k(s, k, index + 1, current)

subsequence_k("acd", 2)
