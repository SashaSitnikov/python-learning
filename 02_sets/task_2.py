skills = set(['english', 'box', 'programming'])
skills.add('basketball')
skills.discard('box')
skills.remove('football')

# remove - удаляет выбранный элемент, если такого элемента нет - ошибка KeyError
# discard - удаляет выбранный элемент, если такого элемента нет - ничего не происходит