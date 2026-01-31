marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# print(marks)
# print(marks["Alice"])
# print('Marks:',marks.items())
# marks["David"] = 88
# print(marks)
# print('Keys:',marks.keys())
# print('Values:',marks.values())
marks.update({"Alice": 92, "Eve": 95})
print(marks)

print('Bob:', marks.get("Bob"))
print('Bob:', marks.get("Bob123")) # None
# print(marks["Bob123"]) # KeyError