#!/usr/bin/env python3

from labyrinth_game.constants import COMMANDS, ROOM_TREASURE
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)

from . import constants as const

game_state = {
    'player_inventory': [],  # Инвентарь игрока
    'current_room': 'entrance',  # Текущая комната
    'game_over': False,  # Значения окончания игры
    'steps_taken': 0  # Количество шагов
}


def process_command(game_state, command):
    """
    Обрабатывает введенную пользователем команду и вызывает соответствующую
     игровую логику.

    Функция анализирует команду, разделяет ее на части и, используя
    конструкцию match-case, определяет, какое действие должен выполнить игрок.

    Args:
        game_state (dict): Словарь, содержащий текущее состояние игры.
        command (str): Строка с командой, введенной пользователем.
    """
    command_list = command.strip().lower().split()
    if not command_list:
        print('Отсутствует аргумент')
        return

    match command_list[0]:

        case const.CMD_LOOK:
            describe_current_room(game_state)

        case const.CMD_USE:
            if len(command_list) < 2 or not command_list[1]:
                print('Нет предмета')
            else:
                use_item(game_state, command_list[1])

        case const.CMD_SOLVE:
            if (game_state[const.CURRENT_ROOM].strip().casefold()
                    == ROOM_TREASURE.strip().casefold()):
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)

        case const.DIR_NORTH | const.DIR_SOUTH | const.DIR_EAST | const.DIR_WEST:
            move_player(game_state, command_list[0])

        case const.CMD_GO:
            if len(command_list) < 2 or not command_list[1]:
                print('Некуда идти')
            else:
                move_player(game_state, command_list[1])

        case const.CMD_INVENTORY:
            show_inventory(game_state)

        case const.CMD_TAKE:
            if len(command_list) < 2 or not command_list[1]:
                print('Нет предмета')
            else:
                take_item(game_state, command_list[1])

        case const.CMD_QUIT | const.CMD_EXIT:
            game_state[const.GAME_OVER] = True

        case const.CMD_HELP:
            show_help(COMMANDS)

        case _:
            print('Команда не найдена!')


def main():
    """
    Главная функция игры: приветствие, первичное описание комнаты и
    основной игровой цикл до завершения игры.
    """
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    while not game_state[const.GAME_OVER]:
        user_input = get_input()
        process_command(game_state, user_input)


if __name__ == '__main__':
    main()
