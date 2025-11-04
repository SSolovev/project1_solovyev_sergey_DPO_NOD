# labyrinth_game/constants.py

ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. '
                       'На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room', 'south': 'kitchen'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным '
                       'сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': (
            'На пьедестале надпись: "Назовите число, которое идет после девяти". '
            'Введите ответ цифрой или словом.',
            ['10', 'десять'])
    },
    'trap_room': {
        'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись:'
                       ' "Осторожно — ловушка".',
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза'
                   ' подряд (введите "шаг шаг шаг")',
                   ['шаг шаг шаг'])
    },
    'library': {
        'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может'
                       ' быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient_book'],
        'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?"'
                   ' (ответ одно слово)', ['резонанс'])
    },
    'armory': {
        'description': 'Старая оружейная комната. На стене висит меч,'
                       ' рядом — небольшая бронзовая шкатулка.',
        'exits': {'south': 'library'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None
    },
    'treasure_room': {
        'description': 'Комната, на столе большой сундук. Дверь заперта — '
                       'нужен особый ключ.',
        'exits': {'south': 'hall'},
        'items': ['treasure_chest'],
        'puzzle': ('Дверь защищена кодом. Введите код (подсказка: это число '
                   'пятикратного шага, 2*5= ? )',
                   ['10', 'десять'])
    },
    'kitchen': {
        'description': 'Кухня, стены выложены белой плиткой, в углу мерцает тусклая '
                       'лампа. В комнате витает странный запах..',
        'exits': {'east': 'hall', 'west': 'cellar'},
        'items': ['knife'],
        'puzzle': None
    },
    'cellar': {
        'description': 'Сырой и мрачный погреб. Посередине комнаты на крюке висят '
                       'части того что когда-то было человеком',
        'exits': {'east': 'kitchen'},
        'items': [],
        'puzzle': (
            'При попытке осмотреть останки, холодные веки поднимаются и на вас смотрят,'
            ' не моргая, два мутных глаза... "Без окон без дверей. '
            'Полна горница людей?" - вопрошает тело',
            ['огурец']),
        'reward': 'treasure_key'
    }
    # ... добавьте сюда остальные комнаты
}

QUIT_GAME = 'quit'


# game_state ключи
class GameState:
    INVENTORY = 'player_inventory'  # Инвентарь игрока
    CURRENT_ROOM = 'current_room'  # Текущая комната
    GAME_OVER = 'game_over'  # Значения окончания игры
    STEPS_TAKEN = 'steps_taken'  # Количество шагов


# константы для названий комнаты
ROOM_TREASURE = 'treasure_room'
TRAP_ROOM = 'trap_room'


# константы для ITEMS комнаты
class Room:
    DESCR = 'description'
    EXITS = 'exits'
    ITEMS = 'items'
    PUZZLE = 'puzzle'
    REWARD = 'reward'


# константы для ITEMS игрока
class Items:
    TORCH = 'torch'  # Предмет Факел
    SWORD = 'sword'
    BRONZE_BOX = 'bronze_box'
    RUSTY_KEY = 'rusty_key'
    TREASURE_KEY = 'treasure_key'
    COIN = 'coin'


TREASURE_CHEST = 'treasure_chest'

COMMANDS = {
    "go <direction>": " перейти в направлении (north/south/east/west)",
    "look": "осмотреть текущую комнату",
    "take <item>": "поднять предмет",
    "use <item>": "использовать предмет из инвентаря",
    "inventory": "показать инвентарь",
    "solve": "попытаться решить загадку в комнате",
    "quit": "выйти из игры",
    "help": "показать это сообщение"
}
