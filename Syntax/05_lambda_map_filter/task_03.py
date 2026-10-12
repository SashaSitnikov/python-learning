numbers = [5, -2, 8, -1, 0, 3]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

chars = ["a", "", "b", "", "c"]
letters = list(filter(None, chars))
print(letters)