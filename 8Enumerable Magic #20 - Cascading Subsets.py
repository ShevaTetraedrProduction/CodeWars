def each_cons(lst, n):
    return [lst[i: i + n] for i in range(0, len(lst), n)]

print(each_cons([3, 5, 8, 13], 2))
