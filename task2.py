import os

def get_cats_info(path):
    with open(path, 'r') as file:
        cats = []
        lines = [line.strip() for line in file.readlines()]
        for line in lines:
            data = line.split(',')
            cat = {'id': data[0], 'name': data[1], 'age': data[2]}
            cats.append(cat)
    return cats

path = 'cats.txt'

if os.path.exists(path):
    cats_info = get_cats_info(path)
    print(cats_info)
else:
    print('File not found or corrupt')