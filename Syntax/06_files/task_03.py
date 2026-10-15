words = 0
chars = 0

with open("text.txt", "w", encoding="utf-8") as f:
    f.write("My name is Alex. I enjoy learning Python and solving programming problems.\n")
    f.write("Every day, I try to learn something new. Sometimes I make mistakes, but I never give up.\n")
    f.write("In the future, I want to become a good programmer.\n")
    
with open("text.txt", "r", encoding="utf-8") as f:
    strings = f.readlines()
    for s in strings:
        words += len(s.split())
        chars += len(s.rstrip())
    print(len(strings))
    print(words)
    print(chars)