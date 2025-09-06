import os

# Функция для очистки консоли
def clear_console():
    # Выполнение команды очистки консоли в зависимости от операционной системы
    os.system('cls' if os.name == 'nt' else 'clear')


# Функция для получения выбора игрока
def get_player_choice(player_num):
    choices = ['камень', 'ножницы', 'бумага']  # Возможные варианты выбора
    while True:
        print(f"Игрок {player_num}, ваш ход (камень, ножницы, бумага): ", end="")
        choice = input().lower()  # Получение ввода игрока и преобразование его к нижнему регистру
        if choice in choices:  # Проверка, что выбор игрока допустим
            return choice  # Возврат выбора игрока
        else:
            print("Неверный ввод. Попробуйте снова.")  # Сообщение об ошибке и повторный запрос ввода


# Функция для определения победителя
def determine_winner(player_choices):
    # Условия победы: ключ побеждает значение
    win_conditions = {
        'камень': 'ножницы',
        'ножницы': 'бумага',
        'бумага': 'камень'
    }
    winners = []  # Список победителей
    for i, choice in enumerate(player_choices):
        is_winner = True
        for other_choice in player_choices:
            # Проверка, что выбор игрока побеждает каждый другой выбор
            if choice != other_choice and win_conditions[choice] != other_choice:
                is_winner = False
                break
        if is_winner:
            winners.append(i + 1)  # Добавление победителя в список (нумерация с 1)
    return winners


# Основная функция
def main():
    print("Добро пожаловать в игру 'Камень, Ножницы, Бумага'!")

    # Защита от неверного ввода количества игроков
    while True:
        try:
            num_players = int(input("Введите количество игроков: "))  # Запрос количества игроков
            if num_players < 2:
                print("Количество игроков должно быть не менее 2. Попробуйте снова.")
            else:
                break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите целое число.")

    player_choices = []  # Список для хранения выборов игроков

    for player_num in range(1, num_players + 1):
        clear_console()  # Очистка консоли перед ходом каждого игрока
        choice = get_player_choice(player_num)  # Получение выбора игрока
        player_choices.append(choice)  # Добавление выбора в список

    clear_console()  # Очистка консоли перед выводом результатов
    winners = determine_winner(player_choices)  # Определение победителя

    print("Ходы игроков:")
    for i, choice in enumerate(player_choices):
        print(f"Игрок {i + 1}: {choice}")  # Вывод ходов всех игроков

    if len(winners) == 1:
        print(f"Победитель: Игрок {winners[0]}")  # Вывод победителя
    elif len(winners) > 1:
        print(f"Ничья между игроками: {', '.join(map(str, winners))}")  # Вывод ничьи
    else:
        print("Нет победителя, все ходы привели к ничье.")  # Если нет победителя


if __name__ == "__main__":
    main()  # Запуск основной функции