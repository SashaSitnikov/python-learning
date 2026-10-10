text = "Hello, World! 123"
letters = [i.lower() for i in text if i.isalpha()]
print(*letters, sep='')

