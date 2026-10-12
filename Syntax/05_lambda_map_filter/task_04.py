# 1
fruits = ["banana", "kiwi", "apple", "fig", "cherry"]
fruits_one = sorted(fruits, key=len)
print(fruits_one)

# 2
fruits_two = sorted(fruits, key=lambda x: (len(x), x))
print(fruits_two)

# 3
fruits_three = sorted(fruits, key=len, reverse=True)
print(fruits_three)