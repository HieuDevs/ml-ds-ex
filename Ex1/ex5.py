# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [
    [4, 3, 5],
    [1, 2, 3],
    [3, 7, 4],
]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]


def resolve():
    print([data5_list1[i] + data5_list2[i] for i in range(len(data5_list1))])
