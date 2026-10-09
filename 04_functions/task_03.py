def rectangle(a, b):
    p = a * 2 + b * 2
    s = a * b
    return p, s


perimeter, area = rectangle(17, 3)
print(perimeter, area)