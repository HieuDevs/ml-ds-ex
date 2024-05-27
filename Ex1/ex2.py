# Ex2: Given a list, extract all elements whose frequency is greater than k.
data = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3


def resolve():
    print([num for num in set(data) if data.count(num) > k])
