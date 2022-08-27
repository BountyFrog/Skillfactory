# Словарь поля для начала партии
start_game_field = {(0, 0): ' ', (0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 0): 1, (1, 1): '_', (1, 2): '_', (1, 3): '_',
                    (2, 0): 2, (2, 1): '_', (2, 2): '_', (2, 3): '_', (3, 0): 3, (3, 1): '_', (3, 2): '_', (3, 3): '_'}
# Пустой словарь для текущей партии
game_field = {}
# Выигрышные комбинации
win_comb = (((1, 1), (1, 2), (1, 3)),
            ((2, 1), (2, 2), (2, 3)),
            ((3, 1), (3, 2), (3, 3)),
            ((1, 1), (2, 1), (3, 1)),
            ((1, 2), (2, 2), (3, 2)),
            ((1, 3), (2, 3), (3, 3)),
            ((1, 1), (2, 2), (3, 3)),
            ((1, 3), (2, 2), (3, 1)))

player1_symbol = 'X'
player2_symbol = 'O'

count_step = 0


def print_game_field():                 # Функция печати поля
    print(f'{game_field[(0, 0)]} {game_field[(0, 1)]} {game_field[(0, 2)]} {game_field[(0, 3)]}')
    print(f'{game_field[(1, 0)]} {game_field[(1, 1)]} {game_field[(1, 2)]} {game_field[(1, 3)]}')
    print(f'{game_field[(2, 0)]} {game_field[(2, 1)]} {game_field[(2, 2)]} {game_field[(2, 3)]}')
    print(f'{game_field[(3, 0)]} {game_field[(3, 1)]} {game_field[(3, 2)]} {game_field[(3, 3)]}')


def check_win_comb(symbol):                                     # Функция проверки выигрышной комбинации.
    player_comb = []
    for x, y in game_field.items():
        if y == symbol:
            player_comb.append(x)
    count = 0
    for value in win_comb:                                      # Цикл проверки выигрышной комбинации
        if set(win_comb[count]).issubset(set(player_comb)):
            print_game_field()
            print(f'Победа "{symbol}"!')
            start_new_game()
        count += 1


def turn(symbol):
    print_game_field()
    coord = tuple(map(int, input(f'Игрок "{symbol}" введите координаты поля через пробел:').split()))
    if game_field[coord] == 'X' or 'O' in game_field[coord]:
        print('Поле занято или неверный формат')
        return turn(symbol)
    else:
        game_field[coord] = symbol
        check_win_comb(symbol)
        global count_step
        count_step += 1
        if count_step < 9:
            if count_step % 2 == 1:
                return turn(player2_symbol)
            else:
                return turn(player1_symbol)
        else:
            print_game_field()
            print(f'Ничья!')
            start_new_game()


def start_new_game():                                           # Функция начала новой игры
    print('Начать новую игру? (Да/Нет):')
    answer = input()
    if answer == 'Да':
        global game_field
        game_field = start_game_field.copy()
        global count_step
        count_step = 0
        turn(player1_symbol)
    elif answer == 'Нет':
        quit()
    else:
        start_new_game()


start_new_game()
