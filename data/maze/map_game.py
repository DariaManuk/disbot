from settings import *
from level_maps import *

world_map = set()
wall_type_map = dict()

fin_pos = (0, 0)


def map_layout(text_map):
    global fin_pos, world_map, wall_type_map
    world_map = set()
    wall_type_map = dict()
    for j, row in enumerate(text_map):
        for i, char in enumerate(row):
            if char == 'P':
                player_pos[0] = i * TILE + TILE // 2
                player_pos[1] = j * TILE + TILE // 2
            elif char == 'F':
                fin_pos = (i * TILE, j * TILE)
            elif char != '.':
                world_map.add((i * TILE, j * TILE))
                wall_type_map[str((i * TILE, j * TILE))] = int(char)
    return world_map, wall_type_map


def change_level(level_num):
    global fin_pos, world_map, wall_type_map
    if level_num == 0:
        world_map, wall_type_map = map_layout(maps["default_map"])
    else:
        world_map, wall_type_map = map_layout(maps[f"level_{level_num}_map"])


# map_layout(maps["level_4_map"])
# print('"level 1": {', end="")
# print('"wall_map":', world_map)
# print('"type_map":', wall_type_map)
# print('"fin_pos":', fin_pos, end="},")
