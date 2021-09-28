table = [[' - ']*3 for _ in range(3)]   # создания заполнения игрового стола

def show_table(t):              # создание игрового стола
    title = "   0   1   2"
    print(title)
    for col, row in zip(title.split(), table):
        print(f"{col} {' '.join(j for j in row)}")

def player_input(t):            # игровой ход
    while True:
        place = input('Ваш ход, введите координаты: ').split()
        if len(place) != 2:
            print("Введите две координаты")
            continue

        if not(place[0].isdigit() and place[1].isdigit()):
            print("Введите числовые координаты")
            continue

        x, y = int(place[0]), int(place[1])
        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("Введите числовые координаты от 0 до 2")
            continue

        if t[y][x] != " - ":
            print("Клетка занята, выберите другую")
            continue

        break
    return x, y

def win(t, player):            # правила победы
    def check_line(a1, a2, a3, player):
        if a1 == player and a2 == player and a3 == player:
            return True
    for n in range(3):
        if check_line(t[n][0], t[n][1], t[n][2], player) or \
           check_line(t[0][n], t[1][n], t[2][n], player) or \
           check_line(t[0][0], t[1][1], t[2][2], player) or \
           check_line(t[2][0], t[1][1], t[0][2], player):
            return True
        return False

count = 0
while True:
    if count == 9:
        show_table(table)
        print("Ничья")
        break
    if count % 2 == 0:
        print("Ходит игрок №1 (х)")
        player = " x "
    else:
        print("Ходит игрок №2 (0)")
        player = " 0 "
    show_table(table)
    x, y = player_input(table)
    table[y][x] = player
    if win(table,  player):
        show_table(table)
        print(f"Выиграл игрок ходивший {player};)")
        break
    count += 1
