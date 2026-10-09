def make_user(name, **kwargs):
    return {"name": name, **kwargs}


first = make_user('Alex', age=20, city="Минск")
print(first)

dictionary = {'age': 20, 'city': 'Minsk'}
second = make_user('Alex', **dictionary)
print(second)

# я ничего не понял, что ты требуешь от меня в этом задании