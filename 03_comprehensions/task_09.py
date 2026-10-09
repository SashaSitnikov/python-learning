table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(table)
flat = [i for row in table for i in row]
print(flat)

