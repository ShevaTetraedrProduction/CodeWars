def move_zeros(array):
    return [i for i in array if i != 0] + [0] * array.count(0)


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))