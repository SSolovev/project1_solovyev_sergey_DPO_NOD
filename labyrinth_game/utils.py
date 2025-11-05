import math
from math import sin

from . import constants as const
from .constants import (
    EVENT_CHANCE_MODULO,
    EVENT_TRIGGER_VALUE,
    MIN_INVENTORY_FOR_LOSS,
    RANDOM_EVENT_COUNT,
    RANDOM_EVENT_SEED,
    ROOM_TRAP,
    ROOMS,
    TRAP_DAMAGE_MODULO,
    TRAP_DAMAGE_SEED,
    TRAP_DEATH_THRESHOLD,
    TREASURE_CHEST,
)
from .player_actions import add_item, get_input, use_item


def describe_current_room(game_state):
    curr_room = get_current_room(game_state)
    print(curr_room[const.DESCR])
    print("Заметные предметы: ", " ,".join(curr_room[const.ITEMS]))
    print("Выходы: ")
    for key, value in curr_room[const.EXITS].items():
        print(f"{key} - {value}")
    if const.PUZZLE in curr_room and curr_room[const.PUZZLE]:
        print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state):
    curr_room = get_current_room(game_state)
    if curr_room[const.PUZZLE] is None:
        print("Загадок здесь нет.")
    else:
        puzzle = curr_room[const.PUZZLE]
        print(puzzle[0])
        user_answer = get_input("Ваш ответ: ")
        puzzle_answers = puzzle[1]

        while (not game_state[const.GAME_OVER]
               and user_answer.strip().casefold() not in puzzle_answers):
            if ROOM_TRAP == game_state[const.CURRENT_ROOM]:
                trigger_trap(game_state)
            print("Неверно. Попробуйте снова.")
            user_answer = get_input("Ваш ответ: ")
            if user_answer == 'exit' or user_answer == 'quit':
                game_state[const.GAME_OVER] = True
        else:
            print("Вы решили загадку!")
            if const.REWARD in curr_room:
                add_item(game_state, curr_room[const.REWARD])
                print("Награда за головоломку добавлена в инвентарь!")
            del curr_room[const.PUZZLE]


def get_current_room(game_state: dict) -> dict:
    curr_room_name = game_state[const.CURRENT_ROOM]
    curr_room = ROOMS[curr_room_name]
    return curr_room


def attempt_open_treasure(game_state):
    inventory = game_state[const.INVENTORY]
    solved = False
    if const.TREASURE_KEY in inventory:
        use_item(game_state, const.TREASURE_KEY)
        get_current_room(game_state)[const.ITEMS].remove(TREASURE_CHEST)
        solved = True
    else:
        decision = get_input("Сундук заперт. ... Ввести код? (да/нет)")
        if decision == 'да':
            solve_puzzle(game_state)
            solved = True
        else:
            print("Вы отступаете от сундука.")
    if solved:
        print(f"В сундуке сокровище! Вы победили! Число шагов: "
              f"{game_state[const.STEPS_TAKEN]}")
        game_state[const.GAME_OVER] = True


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
    inventory_size = len(game_state[const.INVENTORY])
    if inventory_size >= MIN_INVENTORY_FOR_LOSS:
        val = pseudo_random(game_state[const.STEPS_TAKEN], inventory_size)
        item = game_state[const.INVENTORY][val]
        game_state[const.INVENTORY].remove(item)
        print(f"Вы потеряли {item}!")
    else:
        damage = pseudo_random(TRAP_DAMAGE_SEED, TRAP_DAMAGE_MODULO)
        if damage < TRAP_DEATH_THRESHOLD:
            print(
                "Вы не удержали равновесие и упали в пропасть... Игра окончена."
            )
            game_state[const.GAME_OVER] = True
        else:
            print(f"Вы уцелели, но получили повреждения {damage}!")


def random_event(game_state: dict):
    """
    Определяет, произойдет ли случайное событие, и если да, то какое.
    Вызывается после каждого перемещения игрока.
    """
    seed = game_state[const.STEPS_TAKEN]
    event_chance = pseudo_random(seed, EVENT_CHANCE_MODULO)
    if event_chance != EVENT_TRIGGER_VALUE:
        return

    chosen_event = pseudo_random(RANDOM_EVENT_SEED, RANDOM_EVENT_COUNT)

    print("...во время вашего путешествия происходит нечто неожиданное...")

    match chosen_event:
        case const.EVENT_ID_COIN:
            print("Вы замечаете что-то блестящее на полу... Это монетка!")
            get_current_room(game_state)[const.ITEMS].append(const.COIN)

        case const.EVENT_ID_RUSTLE:
            print("В тенях что-то шуршит... вы замерли на месте.")
            if const.SWORD in game_state[const.INVENTORY]:
                print(
                    "Вы выхватываете меч, и шорох тут же прекращается."
                    " Существо отступило."
                )

        case const.EVENT_ID_TRAP:
            if (
                    game_state[const.CURRENT_ROOM] == ROOM_TRAP
                    and const.TORCH not in game_state[const.INVENTORY]
            ):
                print("Вы наступили на шаткую плиту в темноте!")
                trigger_trap(game_state)
