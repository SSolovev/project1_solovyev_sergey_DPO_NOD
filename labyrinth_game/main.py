#!/usr/bin/env python3
from labyrinth_game.constants import QUIT_GAME, GAME_CURRENT_ROOM, ROOM_TREASURE
from labyrinth_game.player_actions import show_inventory, get_input, move_player, take_item, use_item
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows,
# actions, and settings.

from labyrinth_game.utils import describe_current_room, attempt_open_treasure, solve_puzzle

game_state = {
    'player_inventory': [],  # Инвентарь игрока
    'current_room': 'entrance',  # Текущая комната
    'game_over': False,  # Значения окончания игры
    'steps_taken': 0  # Количество шагов
}


def process_command(game_state, command):
    command_list = command.split()

    match command_list[0]:
        case 'look':
            describe_current_room(game_state)
        case 'use':
            use_item(game_state, command_list[1])
        case 'solve':
            if game_state[GAME_CURRENT_ROOM] == ROOM_TREASURE:
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case 'go':
            move_player(game_state, command_list[1])
        case 'inventory':
            show_inventory(game_state)
        case 'take':
            take_item(game_state, command_list[1])
        case 'quit' | 'exit':
            game_state['game_over'] = True


def main():
    # Use a breakpoint in the code line below to debug your script.
    print("Добро пожаловать в Лабиринт сокровищ!")
    current_room = game_state['current_room']
    user_input = ""
    describe_current_room(game_state)
    while game_state['game_over']:
        user_input = get_input()
        process_command(game_state, user_input)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
