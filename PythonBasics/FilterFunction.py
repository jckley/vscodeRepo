def is_positive(a):
    return a > 0


output = list(filter(is_positive, [1, -2, 3, -4, 5, 6, 0]))
print(output)
