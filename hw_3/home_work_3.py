"""Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера."""


# Игра написана в императивном стиле. Используется структурная и процедурная парадигмы, т.к. есть циклы, ветвления, методы и нет goto


# Инициализация карты
maps = [1,2,3,
        4,5,6,
        7,8,9]

# Инициализация победных линий
victories = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]

# Вывод карты на экран
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])

    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])

    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8]) 

# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol

# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
    return win

# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Первый игрок, ваш ход Х: "))
    else:
        symbol = "O"
        step = int(input("Второй игрок, ваш ход О: "))

    step_maps(step,symbol) # делаем ход в указанную ячейку
    win = get_result() # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not(player1)        

# Игра окончена. Покажем карту. Объявим победителя.        
print_maps()
print("Победил", win) 