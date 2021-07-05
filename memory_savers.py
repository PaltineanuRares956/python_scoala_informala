import copy

print('Memory Savers')
print('-' * 40)

my_lambda = lambda x, y: x + y

my_sum = my_lambda(2, 3)
print('2 + 3 =', my_sum)

players = [

    {
        'first_name': 'John',
        'last_name': 'Doe',
        'rank': 3
    },
    {
        'first_name': 'Kevin',
        'last_name': 'McDonald',
        'rank': 1
    },
    {
        'first_name': 'Brad',
        'last_name': 'Kevin',
        'rank': 4
    }
]

print(players)
sorted_players = sorted(players, key=lambda player: player['rank'])
print(sorted_players)


def check_top_3_player(player):
    updated_player = copy.deepcopy(player)
    updated_player['is_top_3'] = True if player['rank'] <= 3 else False
    return updated_player


top_players = list(map(check_top_3_player, players))
print(top_players)
print('-' * 40)

all_mcdonalds = list(filter(lambda player: player['last_name'] == 'McDonald', players))
print(all_mcdonalds)

print()
print()
print()
print()
print('-' * 40)
print('ZIP')
# zip

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3]
print(zip(letters, numbers))

for t in zip(letters, numbers):
    print(t)

print()
print()
print()
print()
print('-' * 40)
print('ZIP')
# list comprehension

my_numbers = [i for i in range(1, 6)]
squared_numbers = [item**2 for item in my_numbers if item % 2 == 0]
print(my_numbers)
print(squared_numbers)
