with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    
with open("hello.txt", 'r', encoding="utf-8") as f:
    r1 = f.read()
    r2 = f.read()
    print(f"{r1}\n{r2}")
    f.seek(0)
    r3 = f.read()
    print(r3)
    
    
    
    
with open("text.txt", "w", encoding="utf-8") as f:
    f.write("My name is Alex. I enjoy learning Python and solving programming problems.\n")
    f.write("Every day, I try to learn something new. Sometimes I make mistakes, but I never give up.\n")
    f.write("In the future, I want to become a good programmer.\n")
    
with open("text.txt", "r", encoding="utf-8") as f:
    strings = f.readlines()
    f.seek(0)
    text = f.readline()
    print(type(strings))
    print(text, end="")
    
    for line in f:
        print(line, end="")
        