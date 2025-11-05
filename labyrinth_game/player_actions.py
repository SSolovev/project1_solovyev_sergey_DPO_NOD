from typing import Dict

from . import constants as const
from .constants import QUIT_GAME, ROOM_TREASURE, ROOMS


def move_player(game_state, direction) -> None:
    """
        Перемещает игрока в другую комнату в указанном направлении.

        Проверяет, существует ли выход в заданном направлении. Если да,
        обновляет текущую комнату игрока и увеличивает счетчик шагов.
        Также обрабатывает особые условия, такие как запертые двери.

        Args:
            game_state (dict): Словарь, содержащий текущее состояние игры.
            direction (str): Направление для перемещения ('north', 'south', и т.д.).
        """
    from labyrinth_game.utils import describe_current_room

    from .utils import random_event
    room_name = game_state[const.CURRENT_ROOM]
    exits = ROOMS[room_name][const.EXITS]
    if direction in exits:
        next_room = exits[direction]
        is_go = True
        if (direction == ROOM_TREASURE and const.RUSTY_KEY
                in game_state[const.INVENTORY]):
            print("Вы используете найденный ключ, "
                  "чтобы открыть путь в комнату сокровищ.")
        elif direction == ROOM_TREASURE:
            print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
            is_go = False

        if is_go:
            game_state[const.CURRENT_ROOM] = next_room
            game_state[const.STEPS_TAKEN] += 1
            describe_current_room(game_state)
            random_event(game_state)
    else:
        print("Нельзя пойти в этом направлении.")



TAKE_ITEMS_EXCEPTIONS = {'treasure_chest': 'Вы не можете поднять сундук,'
                                           ' он слишком тяжелый.'}

def take_item(game_state, item_name) -> None:
    """
    Позволяет игроку взять предмет, находящийся в текущей комнате.

    Перемещает указанный предмет из списка предметов комнаты в инвентарь
    игрока. Обрабатывает случаи, когда предмет нельзя взять.

    Args:
        game_state (dict): Словарь с состоянием игры.
        item_name (str): Название предмета, который нужно взять.
    """
    room_name = game_state[const.CURRENT_ROOM]
    items_list = ROOMS[room_name][const.ITEMS]
    if item_name in items_list and item_name not in TAKE_ITEMS_EXCEPTIONS:
        game_state[const.INVENTORY].append(item_name)
        items_list.remove(item_name)
        print("Вы подняли:", item_name)
    elif item_name in TAKE_ITEMS_EXCEPTIONS:
        print(TAKE_ITEMS_EXCEPTIONS[item_name])
    else:
        print("Такого предмета здесь нет.", item_name)


def show_inventory(game_state: dict) -> None:
    """
    Печатает строку с описанием инвентаря игрока из game_state.

    :param game_state: Словарь с состоянием игры.
    """
    inventory = game_state[const.INVENTORY]
    if not inventory:
        print("Инвентарь пуст!")
    else:
        print(*inventory, sep=', ')


def use_item(game_state: Dict[str, any], item_name: str) -> None:
    """
    Использует предмет из инвентаря, если он есть.

    :param game_state: Словарь с состоянием игры.
    :param item_name: Название предмета.
    """

    inventory_items = game_state[const.INVENTORY]

    if item_name in inventory_items:
        match item_name:
            case const.TORCH:
                print("Стало светлее.")
                inventory_items.remove(item_name)
            case const.SWORD:
                print("Вы стали увереннее.")
                inventory_items.remove(item_name)
            case const.BRONZE_BOX:
                print("Шкатулка открылась. Внутри вы обнаружили ржавый ключ.")
                if const.RUSTY_KEY not in inventory_items:
                    inventory_items.append(const.RUSTY_KEY)
                    inventory_items.remove(item_name)
            case const.TREASURE_KEY:
                print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
                inventory_items.remove(item_name)
            case _:
                print("Вы не знаете, как это использовать.")
    else:
        print(f"У вас нет такого предмета: '{item_name}'")


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


def add_item(game_state, item_name):
    """
    Добавляет предмет в инвентарь игрока, избегая дубликатов.

    Args:
        game_state (dict): Словарь с состоянием игры.
        item_name (str): Название добавляемого предмета.
    """
    inventory_items = game_state['player_inventory']
    if item_name not in inventory_items:
        inventory_items.append(item_name)
