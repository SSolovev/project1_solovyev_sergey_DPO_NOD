from labyrinth_game.constants import QUIT_GAME


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
