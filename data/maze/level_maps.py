# 1 green, 2 grey, 3 purple, 4 red, 5 blue
level_num = 4
maps_real = {
    "level 1": {"wall_map": {(500, 200), (0, 100), (400, 0), (200, 100), (700, 200), (600, 0), (800, 400), (1200, 300),
                             (100, 400),
                             (900, 200), (1000, 400), (0, 200), (800, 0), (200, 200), (100, 0), (1000, 0), (300, 400),
                             (1200, 400),
                             (500, 400), (400, 200), (600, 400), (0, 300), (300, 0), (600, 200), (700, 400), (1200, 0),
                             (1000, 100),
                             (500, 0), (700, 0), (0, 400), (900, 400), (200, 400), (800, 200), (1100, 400), (1200, 100),
                             (1000, 200), (0, 0), (900, 0), (200, 0), (1100, 0), (400, 400), (1200, 200), (300, 200)},
                "type_map": {'(0, 0)': 1, '(100, 0)': 1, '(200, 0)': 1, '(300, 0)': 1, '(400, 0)': 1, '(500, 0)': 1,
                             '(600, 0)': 1,
                             '(700, 0)': 1, '(800, 0)': 1, '(900, 0)': 1, '(1000, 0)': 1, '(1100, 0)': 1,
                             '(1200, 0)': 1,
                             '(0, 100)': 4, '(200, 100)': 4, '(1000, 100)': 2, '(1200, 100)': 2, '(0, 200)': 4,
                             '(200, 200)': 4,
                             '(300, 200)': 4, '(400, 200)': 4, '(500, 200)': 4, '(600, 200)': 3, '(700, 200)': 3,
                             '(800, 200)': 3,
                             '(900, 200)': 2, '(1000, 200)': 2, '(1200, 200)': 2, '(0, 300)': 4, '(1200, 300)': 2,
                             '(0, 400)': 1,
                             '(100, 400)': 1, '(200, 400)': 5, '(300, 400)': 1, '(400, 400)': 5, '(500, 400)': 1,
                             '(600, 400)': 5,
                             '(700, 400)': 1, '(800, 400)': 5, '(900, 400)': 1, '(1000, 400)': 5, '(1100, 400)': 1,
                             '(1200, 400)': 1},
                "fin_pos": (100, 100)},
    "level 2": {"wall_map": {(1000, 300), (500, 200), (0, 100), (400, 0), (1200, 700), (800, 800), (600, 0), (100, 800),
                             (1000, 800), (0, 600), (1200, 300), (300, 300), (600, 500), (0, 200), (800, 0), (300, 800),
                             (1200, 800), (100, 0), (1100, 500), (1000, 0), (500, 800), (0, 700), (800, 500),
                             (300, 400), (700, 800), (1200, 400), (1000, 500), (100, 500), (900, 300), (400, 200),
                             (600, 400), (0, 300), (300, 0), (600, 200), (1200, 0), (1000, 100), (500, 0), (0, 800),
                             (900, 800), (1100, 800), (700, 0), (1200, 500), (200, 800), (0, 400), (200, 400),
                             (200, 500), (800, 200), (600, 300), (1200, 100), (1000, 200), (0, 0), (900, 0), (400, 800),
                             (200, 0), (1300, 800), (1100, 0), (600, 800), (1200, 600), (0, 500), (900, 500),
                             (1200, 200), (800, 300), (300, 200)},
                "type_map": {'(0, 0)': 1, '(100, 0)': 1, '(200, 0)': 1, '(300, 0)': 1, '(400, 0)': 1, '(500, 0)': 1,
                             '(600, 0)': 1,
                             '(700, 0)': 1, '(800, 0)': 1, '(900, 0)': 1, '(1000, 0)': 1, '(1100, 0)': 1,
                             '(1200, 0)': 1,
                             '(0, 100)': 4, '(1000, 100)': 3, '(1200, 100)': 4, '(0, 200)': 4, '(300, 200)': 4,
                             '(400, 200)': 4,
                             '(500, 200)': 4, '(600, 200)': 3, '(800, 200)': 3, '(1000, 200)': 3, '(1200, 200)': 4,
                             '(0, 300)': 4,
                             '(300, 300)': 4, '(600, 300)': 3, '(800, 300)': 3, '(900, 300)': 3, '(1000, 300)': 3,
                             '(1200, 300)': 4,
                             '(0, 400)': 4, '(200, 400)': 4, '(300, 400)': 4, '(600, 400)': 3, '(1200, 400)': 4,
                             '(0, 500)': 4,
                             '(100, 500)': 4, '(200, 500)': 4, '(600, 500)': 3, '(800, 500)': 3, '(900, 500)': 3,
                             '(1000, 500)': 4,
                             '(1100, 500)': 4, '(1200, 500)': 4, '(0, 600)': 4, '(1200, 600)': 2, '(0, 700)': 4,
                             '(1200, 700)': 2,
                             '(0, 800)': 1, '(100, 800)': 1, '(200, 800)': 1, '(300, 800)': 1, '(400, 800)': 1,
                             '(500, 800)': 1,
                             '(600, 800)': 1, '(700, 800)': 1, '(800, 800)': 1, '(900, 800)': 1, '(1000, 800)': 1,
                             '(1100, 800)': 1,
                             '(1200, 800)': 1, '(1300, 800)': 1},
                "fin_pos": (100, 400)},
    "level 3": {"wall_map": {(500, 200), (0, 100), (400, 0), (700, 200), (1200, 700), (800, 800), (600, 0), (100, 800),
                             (1000, 800), (0, 600), (800, 400), (1200, 300), (1000, 400), (0, 200), (800, 0),
                             (300, 800), (200, 200), (1200, 800), (600, 100), (100, 0), (1000, 0), (500, 800), (0, 700),
                             (800, 500), (300, 400), (700, 800), (1200, 400), (1000, 500), (500, 400), (400, 200),
                             (600, 400), (0, 300), (300, 0), (600, 200), (700, 400), (1200, 0), (1000, 100), (500, 0),
                             (0, 800), (900, 800), (800, 600), (1100, 800), (700, 0), (1200, 500), (1000, 600),
                             (200, 800), (0, 400), (200, 400), (800, 200), (1100, 400), (1200, 100), (1000, 200),
                             (0, 0), (900, 0), (400, 800), (200, 0), (1300, 800), (1100, 0), (600, 800), (1200, 600),
                             (0, 500), (400, 400), (1200, 200), (300, 200)},
                "type_map": {'(0, 0)': 1, '(100, 0)': 1, '(200, 0)': 1, '(300, 0)': 1, '(400, 0)': 1, '(500, 0)': 1,
                             '(600, 0)': 1, '(700, 0)': 1, '(800, 0)': 1, '(900, 0)': 1, '(1000, 0)': 1,
                             '(1100, 0)': 1, '(1200, 0)': 1, '(0, 100)': 4, '(600, 100)': 1, '(1000, 100)': 3,
                             '(1200, 100)': 2, '(0, 200)': 4, '(200, 200)': 2, '(300, 200)': 2, '(400, 200)': 4,
                             '(500, 200)': 4, '(600, 200)': 2, '(700, 200)': 1, '(800, 200)': 2, '(1000, 200)': 3,
                             '(1200, 200)': 2, '(0, 300)': 4, '(1200, 300)': 2, '(0, 400)': 4, '(200, 400)': 2,
                             '(300, 400)': 2, '(400, 400)': 2, '(500, 400)': 4, '(600, 400)': 3, '(700, 400)': 1,
                             '(800, 400)': 2, '(1000, 400)': 3, '(1100, 400)': 3, '(1200, 400)': 2, '(0, 500)': 4,
                             '(800, 500)': 3, '(1000, 500)': 4, '(1200, 500)': 2, '(0, 600)': 4, '(800, 600)': 4,
                             '(1000, 600)': 4, '(1200, 600)': 4, '(0, 700)': 4, '(1200, 700)': 4, '(0, 800)': 1,
                             '(100, 800)': 1, '(200, 800)': 1, '(300, 800)': 1, '(400, 800)': 1, '(500, 800)': 1,
                             '(600, 800)': 1, '(700, 800)': 1, '(800, 800)': 1, '(900, 800)': 1, '(1000, 800)': 1,
                             '(1100, 800)': 1, '(1200, 800)': 1, '(1300, 800)': 1},
                "fin_pos": (500, 100)},
    "level 4": {"wall_map": {(100, 300), (1000, 300), (0, 100), (400, 0), (700, 200), (1200, 700), (800, 800), (600, 0),
                             (100, 800), (1000, 800), (0, 600), (800, 400), (400, 500), (1200, 300), (200, 600),
                             (300, 300), (100, 400), (900, 200), (1000, 400), (0, 200), (800, 0), (300, 800),
                             (1200, 800), (100, 0), (400, 600), (1000, 0), (500, 800), (0, 700), (800, 500), (700, 800),
                             (1200, 400), (200, 700), (500, 400), (600, 600), (0, 300), (300, 0), (600, 200),
                             (700, 400), (1200, 0), (1000, 100), (500, 0), (0, 800), (900, 800), (800, 600), (300, 500),
                             (600, 700), (700, 0), (1200, 500), (1000, 600), (200, 800), (0, 400), (1100, 800),
                             (400, 300), (800, 200), (100, 200), (1200, 100), (1000, 200), (0, 0), (900, 0), (400, 800),
                             (200, 0), (1300, 800), (1100, 0), (300, 600), (600, 800), (1200, 600), (1000, 700),
                             (0, 500), (700, 600), (1200, 200), (300, 200)},
                "type_map": {'(0, 0)': 1, '(100, 0)': 1, '(200, 0)': 1, '(300, 0)': 1, '(400, 0)': 1, '(500, 0)': 1,
                             '(600, 0)': 1, '(700, 0)': 1, '(800, 0)': 1, '(900, 0)': 1, '(1000, 0)': 1, '(1100, 0)': 1,
                             '(1200, 0)': 1, '(0, 100)': 4, '(1000, 100)': 1, '(1200, 100)': 2, '(0, 200)': 4,
                             '(100, 200)': 1, '(300, 200)': 1, '(600, 200)': 1, '(700, 200)': 2, '(800, 200)': 2,
                             '(900, 200)': 3, '(1000, 200)': 3, '(1200, 200)': 2, '(0, 300)': 4, '(100, 300)': 1,
                             '(300, 300)': 1, '(400, 300)': 1, '(1000, 300)': 3, '(1200, 300)': 2, '(0, 400)': 4,
                             '(100, 400)': 1, '(500, 400)': 2, '(700, 400)': 2, '(800, 400)': 2, '(1000, 400)': 3,
                             '(1200, 400)': 2, '(0, 500)': 4, '(300, 500)': 2, '(400, 500)': 2, '(800, 500)': 2,
                             '(1200, 500)': 2, '(0, 600)': 4, '(200, 600)': 1, '(300, 600)': 2, '(400, 600)': 3,
                             '(600, 600)': 3, '(700, 600)': 3, '(800, 600)': 3, '(1000, 600)': 3, '(1200, 600)': 4,
                             '(0, 700)': 4, '(200, 700)': 1, '(600, 700)': 1, '(1000, 700)': 1, '(1200, 700)': 4,
                             '(0, 800)': 1, '(100, 800)': 1, '(200, 800)': 1, '(300, 800)': 1, '(400, 800)': 1,
                             '(500, 800)': 1, '(600, 800)': 1, '(700, 800)': 1, '(800, 800)': 1, '(900, 800)': 1,
                             '(1000, 800)': 1, '(1100, 800)': 1, '(1200, 800)': 1, '(1300, 800)': 1},
                "fin_pos": (100, 700)}
}
maps = {
    "default_map": [
        '1111111111111',
        '1...........2',
        '2...........1',
        '3...........5',
        '4.....P.....4',
        '5...........3',
        '1...........2',
        '2...........1',
        '1111111111111'
    ],
    "level_1_map": [
        '1111111111111',
        '4F4.......2P2',
        '4.444433322.2',
        '4...........2',
        '1151515151511'
    ],
    "level_2_map": [
        '1111111111111',
        '4.........3P4',
        '4..4443.3.3.4',
        '4..4..3.333.4',
        '4F44..3.....4',
        '444...3.33444',
        '4...........2',
        '4...........2',
        '11111111111111'
    ],
    "level_3_map": [
        '1111111111111',
        '4....F1...3P2',
        '4.2244212.3.2',
        '4...........2',
        '4.2224312.332',
        '4.......3.4.2',
        '4.......4.4.4',
        '4...........4',
        '11111111111111'
    ],
    "level_4_map": [
        '1111111111111',
        '4.........1P2',
        '41.1..12233.2',
        '41.11.....3.2',
        '41...2.22.3.2',
        '4..22...2...2',
        '4.123.333.3.4',
        '4F1...1...1.4',
        '11111111111111'
    ]
}
