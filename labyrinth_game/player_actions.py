from labyrinth_game.constants import QUIT_GAME


def show_inventory(game_state):
    inventory=game_state['player_inventory']
    if not inventory:
        print("Инвентарь пуст!")
    else:
        print(*inventory, sep=', ')

def get_input(prompt="> "):
    try:
        input_str=input("Введите данные: ")
        return input_str
    except(KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return QUIT_GAME