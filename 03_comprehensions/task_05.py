numbers = [1, 2, 3, 4, 5, 6]
lst = [0 if i % 2 == 0 else i for i in numbers]
print(*lst)

