with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello\nHello\nHello\n")
    
with open("hello.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)
    