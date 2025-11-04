import math
from math import sin

from .constants import (ROOMS,
                        TREASURE_CHEST, Items, Room, GameState, TRAP_ROOM)
from .player_actions import get_input, add_item, use_item


def describe_current_room(game_state):
    curr_room = get_current_room(game_state)
    print(curr_room[Room.DESCR])
    print("Заметные предметы: ", " ,".join(curr_room[Room.ITEMS]))
    print("Выходы: ")
    for key, value in curr_room[Room.EXITS].items():
        print(f"{key} - {value}")
    if Room.PUZZLE in curr_room and curr_room[Room.PUZZLE]:
        print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state):
    curr_room = get_current_room(game_state)
    if curr_room[Room.PUZZLE] is None:
        print("Загадок здесь нет.")
    else:
        puzzle = curr_room[Room.PUZZLE]
        print(puzzle[0])
        user_answer = get_input("Ваш ответ: ")
        puzzle_answers = puzzle[1]

        while not game_state[GameState.GAME_OVER] and user_answer.strip().casefold() not in puzzle_answers:
            if TRAP_ROOM == game_state[GameState.CURRENT_ROOM]:
                trigger_trap(game_state)
            print("Неверно. Попробуйте снова.")
            user_answer = get_input("Ваш ответ: ")
            if user_answer == 'exit' or user_answer == 'quit':
                game_state[GameState.GAME_OVER] = True
        else:
            print("Вы решили загадку!")
            if Room.REWARD in curr_room:
                add_item(game_state, curr_room[Room.REWARD])
                print("Награда за головоломку добавлена в инвентарь!")
            del curr_room[Room.PUZZLE]


def get_current_room(game_state: dict) -> dict:
    curr_room_name = game_state[GameState.CURRENT_ROOM]
    curr_room = ROOMS[curr_room_name]
    return curr_room


def attempt_open_treasure(game_state):
    inventory = game_state[GameState.INVENTORY]
    solved = False
    if Items.TREASURE_KEY in inventory:
        use_item(game_state, Items.TREASURE_KEY)
        get_current_room(game_state)[Room.ITEMS].remove(TREASURE_CHEST)
        solved = True
    else:
        decision = get_input("Сундук заперт. ... Ввести код? (да/нет)")
        if decision == 'да':
            solve_puzzle(game_state)
            solved = True
        else:
            print("Вы отступаете от сундука.")
    if solved:
        print(f"В сундуке сокровище! Вы победили! Число шагов: {game_state[GameState.STEPS_TAKEN]}")
        game_state[GameState.GAME_OVER] = True


def show_help(commands: dict):
    print("\nДоступные команды:")
    print("-" * 20)
    for command, description in commands.items():
        print(f"{command:<16} - {description}")


def pseudo_random(seed, modulo):
    val = sin(seed) * 12.9898 * 43758.5453
    val = (val - math.floor(val)) * modulo
    return math.floor(val)


def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    modulo = len(game_state[GameState.INVENTORY])
    if modulo > 0:
        val = pseudo_random(game_state[GameState.STEPS_TAKEN], modulo)
        item = game_state[GameState.INVENTORY][val]
        game_state[GameState.INVENTORY].remove(item)
        print(f"Вы потеряли {item}!")
    else:
        damage = pseudo_random(0, 9)
        if damage < 3:
            print("Вы не удержали равновесие и упали в пропасть... Игра окончена.")
            game_state[GameState.GAME_OVER] = True
        else:
            print(f"Вы уцелели, но получили повреждения {damage}!")


def random_event(game_state: dict):
    """
    Определяет, произойдет ли случайное событие, и если да, то какое.
    Вызывается после каждого перемещения игрока.
    """
    seed = game_state[GameState.STEPS_TAKEN]
    event_chance = pseudo_random(seed, 10)
    if event_chance != 0:
        return
    chosen_event = pseudo_random(0, 3)

    print("...во время вашего путешествия происходит нечто неожиданное...")

    match chosen_event:
        case 0:
            print("Вы замечаете что-то блестящее на полу... Это монетка!")
            get_current_room(game_state)[Room.ITEMS].append(Items.COIN)

        case 1:
            print("В тенях что-то шуршит... вы замерли на месте.")
            if Items.SWORD in game_state[GameState.INVENTORY]:
                print("Вы выхватываете меч, и шорох тут же прекращается. Существо отступило.")

        case 2:
            if game_state[GameState.CURRENT_ROOM] == TRAP_ROOM and Items.TORCH not in game_state[GameState.INVENTORY]:
                print("Вы наступили на шаткую плиту в темноте!")
                trigger_trap(game_state)
