from settings import *
from map_game import *


def move_forward(player_pos, player_angle, map):
    world_map = maps_real[f"level {map}"]["wall_map"]
    if player_angle == 0:
        if not ((player_pos[0] + TILE // 2, player_pos[1] - TILE // 2) in world_map):
            player_pos[0] += TILE
        # else:
        # print("no")
    elif player_angle == 2:
        if not ((player_pos[0] - TILE // 2 - TILE, player_pos[1] - TILE // 2) in world_map):
            player_pos[0] -= TILE
        # else:
        # print("no")
    elif player_angle == 3:
        if not ((player_pos[0] - TILE // 2, player_pos[1] - TILE // 2 - TILE) in world_map):
            player_pos[1] -= TILE
        # else:
        # print("no")
    elif player_angle == 1:
        if not ((player_pos[0] - TILE // 2, player_pos[1] + TILE // 2) in world_map):
            player_pos[1] += TILE
        # else:
        # print("no")
    return player_pos, player_angle


def move_back(player_pos, player_angle, map):
    world_map = maps_real[f"level {map}"]["wall_map"]
    # print(player_angle)
    if player_angle == 2:
        if not ((player_pos[0] + TILE // 2, player_pos[1] - TILE // 2) in world_map):
            player_pos[0] += TILE
        # else:
        # print("no")
    elif player_angle == 0:
        if not ((player_pos[0] - TILE // 2 - TILE, player_pos[1] - TILE // 2) in world_map):
            player_pos[0] -= TILE
        # else:
        # print("no")
    elif player_angle == 1:
        if not ((player_pos[0] - TILE // 2, player_pos[1] - TILE // 2 - TILE) in world_map):
            player_pos[1] -= TILE
        # else:
        # print("no")
    elif player_angle == 3:
        if not ((player_pos[0] - TILE // 2, player_pos[1] + TILE // 2) in world_map):
            player_pos[1] += TILE
        # else:
        # print("no")
    return player_pos, player_angle


def move_right(player_pos, player_angle, map):
    world_map = maps_real[f"level {map}"]["wall_map"]
    # print(player_angle)
    if player_angle == 3:
        if not ((player_pos[0] + TILE // 2, player_pos[1] - TILE // 2) in world_map):
            player_pos[0] += TILE
        # else:
        # print("no")
    elif player_angle == 1:
        if not ((player_pos[0] - TILE // 2 - TILE, player_pos[1] - TILE // 2) in world_map):
            player_pos[0] -= TILE
        # else:
        # print("no")
    elif player_angle == 2:
        if not ((player_pos[0] - TILE // 2, player_pos[1] - TILE // 2 - TILE) in world_map):
            player_pos[1] -= TILE
        # else:
        # print("no")
    elif player_angle == 0:
        if not ((player_pos[0] - TILE // 2, player_pos[1] + TILE // 2) in world_map):
            player_pos[1] += TILE
        # else:
        # print("no")
    return player_pos, player_angle


def move_left(player_pos, player_angle, map):
    world_map = maps_real[f"level {map}"]["wall_map"]
    # print(player_angle)
    if player_angle == 1:
        if not ((player_pos[0] + TILE // 2, player_pos[1] - TILE // 2) in world_map):
            player_pos[0] += TILE
        # else:
        # print("no")
    elif player_angle == 3:
        if not ((player_pos[0] - TILE // 2 - TILE, player_pos[1] - TILE // 2) in world_map):
            player_pos[0] -= TILE
        # else:
        # print("no")
    elif player_angle == 0:
        if not ((player_pos[0] - TILE // 2, player_pos[1] - TILE // 2 - TILE) in world_map):
            player_pos[1] -= TILE
        # else:
        # print("no")
    elif player_angle == 2:
        if not ((player_pos[0] - TILE // 2, player_pos[1] + TILE // 2) in world_map):
            player_pos[1] += TILE
        # else:
        # print("no")
    return player_pos, player_angle
