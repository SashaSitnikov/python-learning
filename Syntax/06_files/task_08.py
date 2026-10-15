count = {}

with open("count.txt", "w", encoding="utf-8") as f:
    f.write("My name is Alex. I enjoy learning Python and solving programming problems.\n")
    f.write("Every day, I try to learn something new. Sometimes I make mistakes, but I never give up.\n")
    f.write("In the future, I want to become a good programmer.\n")
    
with open("count.txt", "r", encoding="utf-8") as f:
    for line in f:
        for word in line.rstrip().split():
            word = word.lower().strip(".,!?")
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
                
sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

with open("result.txt", "w", encoding="utf-8") as f:
    for key, value in sorted_count.items():
        f.write(f"{key}: {value}\n")