def digital_root(n):
    a = sum([int(i) for i in str(n)])
    if n < 10: return a
    return digital_root(a)


print(digital_root(493193))