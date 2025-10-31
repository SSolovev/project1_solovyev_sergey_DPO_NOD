# labyrinth_game/constants.py
from labyrinth_game.constants import ROOM_ITEMS

ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': (
            'На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.',
            '10')
    },
    'trap_room': {
        'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")',
                   'шаг шаг шаг')
    },
    'library': {
        'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient_book'],
        'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс')
    },
    'armory': {
        'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
        'exits': {'south': 'library'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None
    },
    'treasure_room': {
        'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
        'exits': {'south': 'hall'},
        'items': ['treasure_chest'],
        'puzzle': ('Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ? )', '10')
    },
    'kitchen': {
        'description': 'Кухня, стены выложены белой плиткой, в углу мерцает тусклая лампа. В комнате витает странный запах..',
        'exits': {'east': 'hall', 'west': 'cellar'},
        'items': ['knife'],
        'puzzle': None
    },
    'cellar': {
        'description': 'Сырой и мрачный погреб. Посередине комнаты на крюке висят части того что когда-то было человеком',
        'exits': {'east': 'kitchen'},
        'items': ['treasure_key'],
        'puzzle': (
            'При попытке осмотреть останки, холодные веки поднимаются и на вас смотрят, не моргая, два мутных глаза... "Без окон без дверей. Полна горница людей?" - вопрошает тело',
            'огурец')
    }
    # ... добавьте сюда остальные комнаты
}

QUIT_GAME = 'quit'

# game_state ключи
GAME_INVENTORY = 'player_inventory'  # Инвентарь игрока
GAME_CURRENT_ROOM = 'current_room'  # Текущая комната
GAME_GAME_OVER = 'game_over'  # Значения окончания игры
GAME_STEPS_TAKEN = 'steps_taken'  # Количество шагов

# константы для названий комнаты
ROOM_TREASURE='treasure_room'

# константы для ITEMS комнаты
ROOM_DESCR='description'
ROOM_EXITS= 'exits'
ROOM_ITEMS='items'
ROOM_PUZZLE='puzzle'

# константы для ITEMS игрока
ITEM_TORCH = 'torch'
ITEM_SWORD = 'sword'
ITEM_BRONZE_BOX = 'bronze_box'
ITEM_RUSTY_KEY = 'rusty_key'


TREASURE_KEY = 'treasure_key'
TREASURE_CHEST = 'treasure_chest'
