import itertools

data = [1, 2, 3]


def resolve():
    for combination in [combination for combination in itertools.permutations(data, 3)]:
        print(combination)
