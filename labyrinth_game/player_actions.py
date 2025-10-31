from os.path import exists
from typing import Dict

from .constants import QUIT_GAME, ROOMS, GAME_INVENTORY, ITEM_TORCH, ITEM_BRONZE_BOX, ITEM_RUSTY_KEY, ITEM_SWORD, TREASURE_KEY

from labyrinth_game.utils import describe_current_room


def use_item(game_state: Dict[str, any], item_name: str) -> None:
    """
    Использует предмет из инвентаря, если он есть.

    :param game_state: Словарь с состоянием игры.
    :param item_name: Название предмета.
    """

    inventory_items = game_state[GAME_INVENTORY]

    if item_name in inventory_items:
        match item_name:
            case ITEM_TORCH:
                print("Стало светлее.")
                inventory_items.remove(item_name)
            case ITEM_SWORD:
                print("Вы стали увереннее.")
                inventory_items.remove(item_name)
            case ITEM_BRONZE_BOX:
                print("Шкатулка открылась. Внутри вы обнаружили ржавый ключ.")
                if ITEM_RUSTY_KEY not in inventory_items:
                    inventory_items.append(ITEM_RUSTY_KEY)
                    inventory_items.remove(item_name)
            case TREASURE_KEY:
                print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
                inventory_items.remove(item_name)
            case _:
                print("Вы не знаете, как это использовать.")
    else:
        print(f"У вас нет такого предмета: '{item_name}'")


def show_inventory(game_state: dict) -> None:
    """
    Печатает строку с описанием инвентаря игрока из game_state.

    :param game_state: Словарь с состоянием игры.
    """
    inventory = game_state['player_inventory']
    if not inventory:
        print("Инвентарь пуст!")
    else:
        print(*inventory, sep=', ')


def get_input(prompt: str = "> ") -> str:
    """
    Получить данные от пользователя

    :param prompt: Параметер для ввода данных
    :return: строка полученная от пользователя
    """
    try:
        user_input = input(prompt)
        return user_input
    except(KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return QUIT_GAME


def move_player(game_state, direction) -> None:
    room_name = game_state['current_room']
    exits = ROOMS[room_name]['exits']
    if exits:
        next_room = exits[direction]
        game_state['current_room'] = next_room
        game_state['steps_taken'] += 1
        describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.")


TAKE_ITEMS_EXCEPTIONS = {'treasure_chest': 'Вы не можете поднять сундук, он слишком тяжелый.'}


def take_item(game_state, item_name) -> None:
    room_name = game_state['current_room']
    items_list = ROOMS[room_name]['items']
    if item_name in items_list and item_name not in TAKE_ITEMS_EXCEPTIONS:
        game_state['player_inventory'].append(item_name)
        items_list.remove(item_name)
        print("Вы подняли:", item_name)
    elif item_name in TAKE_ITEMS_EXCEPTIONS:
        print(TAKE_ITEMS_EXCEPTIONS[item_name])
    else:
        print("Такого предмета здесь нет.", item_name)


def add_item(game_state, item_name):
    inventory_items = game_state['player_inventory']
    if item_name not in inventory_items:
        inventory_items.append(item_name)
