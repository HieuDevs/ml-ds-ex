# Ex1: Write a program to count positive and negative numbers in a list
data = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]


def reslove():
    pos = sum(1 for num in data if num > 0)
    neg = sum(1 for num in data if num < 0)
    print(f"Positive numbers: {pos}")
    print(f"Negative numbers: {neg}")
