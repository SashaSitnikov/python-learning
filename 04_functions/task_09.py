def count_words(text):
    count = {}
    for el in text.split():
        if el.lower() not in count:
            count[el.lower()] = 1
        else:
            count[el.lower()] += 1
            
    return count
    
    
text = 'Cat and dog and snake cat and pig'
print(count_words(text))


