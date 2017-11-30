# creates all possible haiku's from stored 5/7 syllable lines

import itertools

five = ['suki on fat skis', 'onsen, ramen, sleep', 'shred pow on fat lines',
        'arigato, yall', 'arigato, Line', 'floating on a fat line',
        'lets eat some ramen', 'siberian breeze', 'look at that sick Line', 
        'onsen, rinse, repeat', 'old man in summer', 'wait for snow to fall', 
        'ill ski some fish skis', 'party with monkeys']

seven = ['shred pow until jello knees', 'onsen, ramen, more bombin',
         'evo-san, thanks for good times', 'hold my sake, I got this',
         'no pizza, only french fry', 'line skis, onsen, snow monkeys',
         'confusciuis say, wrong country']

two_lines = [five, seven]

first_two = list(itertools.product(*two_lines))

haikus = []

for line in five:
    for two in first_two:
        if line != two[0]:
            haikus.append([two[0], two[1], line])
        else:
            continue

for haiku in haikus:
    print(haiku[0])
    print(haiku[1])
    print(haiku[2])
    print('\n')
