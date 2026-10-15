count = 0

with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello\nHello\nHello\n")
    
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("Hello\n")
    
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        count += 1
        print(f"{count}. {line.rstrip()}")
        