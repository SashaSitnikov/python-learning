def count_words(text):
    count = {}
    for el in text.split():
        word = el.lower()
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
            
    return count
    
    
text = 'Cat and dog and snake cat and pig'
print(count_words(text))


