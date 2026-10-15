count = 0
suma = 0

with open("numbers.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(f'{i}\n')
        
with open("numbers.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            suma += int(line.rstrip())
            count += 1
    print(suma / count)
    print(suma)
    
    