with open("a.txt", "w", encoding="utf-8") as f:
    f.write("Hello")
    
file = open("a.txt", "w", encoding="utf-8")
try:
    file.write("Hello")
finally:
    file.close()
