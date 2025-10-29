#!/usr/bin/env python3
from labyrinth_game.constants import QUIT_GAME
from labyrinth_game.player_actions import show_inventory, get_input
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows,
# actions, and settings.

from labyrinth_game.utils import describe_current_room

game_state = {
    'player_inventory': [],  # Инвентарь игрока
    'current_room': 'entrance',  # Текущая комната
    'game_over': False,  # Значения окончания игры
    'steps_taken': 0  # Количество шагов
}


def main():
    # Use a breakpoint in the code line below to debug your script.
    print("Добро пожаловать в Лабиринт сокровищ!")
    current_room = game_state['current_room']
    user_input = ""
    while user_input.lower() != QUIT_GAME:
        describe_current_room(game_state)
        show_inventory(game_state)
        user_input = get_input(game_state)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
