my_dict = {
    3: "three",
    5: "five",
    9: "nine",
    1: "one",
    4: "four",
    2: "two"
}

my_dict1 = {
    0: "zero",
    False: "false"
}

print(3 in my_dict)
print("three" in my_dict.values())
print(len(my_dict))
print(all(my_dict), any(my_dict))
print(all(my_dict1), any(my_dict1))
print(sorted(my_dict))