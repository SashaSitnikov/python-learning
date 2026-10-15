with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Русский текст для теста")
    
with open("test.txt", "r", encoding="cp1251") as f:
    test = f.read()
    print(test)
