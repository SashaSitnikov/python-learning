text = ["1", "2", "3", "10"]
numbers = list(map(int, text))
print(numbers)



# map + lambda
nums = [1, 2, 3, 4]
square_one = list(map(lambda x: x ** 2, nums))
print(square_one)

# comprehensions
square_two = [el ** 2 for el in nums]
print(square_two)