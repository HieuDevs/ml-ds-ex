# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data = [4, 5, 6, 7, 3, 9, 11, 2, 10]


def resolve():
    print([max(data[i], data[i + 1]) for i in range(len(data) - 1)])
