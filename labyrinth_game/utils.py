from .constants import ROOMS, GAME_INVENTORY, TREASURE_KEY, ROOM_ITEMS, TREASURE_CHEST, GAME_GAME_OVER
from .player_actions import get_input, add_item, use_item


def describe_current_room(game_state):
    curr_room = get_current_room(game_state)
    # print(curr_room_name.upper())
    print(curr_room['description'])
    # print("Заметные предметы: ",', '.join(curr_room['items']))
    print("Заметные предметы: ", *curr_room['items'])
    print("Выходы: ")
    for key, value in curr_room['exits'].items():
        print(f"{key} - {value}")
    if curr_room['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).", curr_room['puzzle'])


def solve_puzzle(game_state):
    curr_room = get_current_room(game_state)
    if curr_room['puzzle'] is None:
        print("Загадок здесь нет.")
    else:
        puzzle = curr_room['puzzle']
        print(puzzle(0))
        user_answer = get_input("Ваш ответ: ")

        while not game_state['game_over'] and user_answer != puzzle(1):
            print("Неверно. Попробуйте снова.")
            user_answer = get_input("Ваш ответ: ")
            if user_answer == 'exit' or user_answer == 'quit':
                game_state['game_over'] = True
        else:
            print("Вы решили загадку!")
            del curr_room['puzzle']
            add_item(game_state, "Награда за головоломку")


def get_current_room(game_state: dict) -> dict:
    curr_room_name = game_state['current_room']
    curr_room = ROOMS[curr_room_name]
    return curr_room

def attempt_open_treasure(game_state):
    inventory = game_state[GAME_INVENTORY]
    if TREASURE_KEY in inventory:
        use_item(game_state, TREASURE_KEY)
        get_current_room(game_state)[ROOM_ITEMS].remove(TREASURE_CHEST)
        print("В сундуке сокровище! Вы победили!")
        game_state[GAME_GAME_OVER] = True
    else:
        decision=get_input("Сундук заперт. ... Ввести код? (да/нет)")
        if decision == 'да':
            solve_puzzle(game_state)
        else:
            print("Вы отступаете от сундука.")
