from .constants import ROOMS


def describe_current_room(game_state):
    curr_room_name = game_state['current_room']
    curr_room = ROOMS[curr_room_name]
    print(curr_room_name.upper())
    print(curr_room['description'])
    # print("Заметные предметы: ",', '.join(curr_room['items']))
    print("Заметные предметы: ", *curr_room['items'])
    print("Выходы: ")
    for key, value in curr_room['exits'].items():
        print(f"{key} - {value}")
    if curr_room['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).", curr_room['puzzle'])
