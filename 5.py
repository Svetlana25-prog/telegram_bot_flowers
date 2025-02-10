name = input('Название цветка: ')

f = open('date.txt', 'r',encoding='utf-8')
flowers = f.read().split('\n')
m = False
for flower in flowers:
    flower_s = flower.split(' - ')
    if flower_s[0] == name:
        m = True
        print(f'{flower_s[1]}')
        break
if not m:
    print('Такого цветка нет!')

