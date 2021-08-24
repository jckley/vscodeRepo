def add_list(a, b, c):
    return a + b + c


output = list(map(add_list, [1, 2, 3], [1, 2, 3, 6], [1, 2, 3]))
print(output)
