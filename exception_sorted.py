numbers = [13, 9, 5, 14]
words = ["mad", "dp", "bh", "bc"]
mixed_list = [1, "c", 3, 2, "a", 8, "b", 4]

numbers.sort()
words.sort()
# mixed_list.sort()  # this was possible in Python2

print(numbers)
print(words)
print(mixed_list)

try:
    mixed_list_sorted = sorted(mixed_list)
    # mixed_list.sort()
except TypeError as err:
    # listInts = sorted([x for x in mixed_list if type(x) is int])
    listInts = []
    listStrs = []
    for x in mixed_list:
        if type(x) is int:
            listInts.append(x)
        elif type(x) is str:
            listStrs.append(x)

    listInts = sorted(listInts)
    listStrs = sorted(listStrs)
    # listStrs = [x for x in mixed_list if type(x) is str]
    # listStrs = sorted([x for x in mixed_list if isinstance(x, str)])
    mixed_list_sorted = listInts + listStrs

print(mixed_list_sorted)
