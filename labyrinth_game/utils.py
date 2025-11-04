from .constants import (ROOMS,
                        TREASURE_CHEST, Items, Room, GameState)
from .player_actions import get_input, add_item, use_item


def describe_current_room(game_state):
    curr_room = get_current_room(game_state)
    # print(curr_room_name.upper())
    print(curr_room[Room.DESCR])
    # print("Заметные предметы: ",', '.join(curr_room[Room.ITEMS]))
    print("Заметные предметы: ", *curr_room[Room.ITEMS])
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
        
        while not game_state[GameState.GAME_OVER] and user_answer.strip().casefold() != puzzle[1].strip().casefold():
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
    solved= False
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
        print("В сундуке сокровище! Вы победили!")
        game_state[GameState.GAME_OVER] = True

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")