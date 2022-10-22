def player_move(row, col):
    if maze_field[row][col] == "E":
        return False, True, False
    elif maze_field[row][col] == "T":
        return False, False, True
    elif maze_field[row][col] == "W":
        return True, False, False

    return False, False, False

size = 6

player_one, player_two = input().split(', ')
maze_field = [[x for x in input().split()] for x in range(size)]
counter = 9
player_one_skips = False
player_two_skips = False

while True:
    position = input()
    row, col = int(position[1]), int(position[4])
    found_the_exit = False
    found_a_trap = False
    hit_a_wall = False

    if counter % 2 != 0:
        if player_one_skips:
            player_one_skips = False
            counter += 1
            continue
        counter += 1
        hit_a_wall, found_the_exit, found_a_trap = player_move(row, col)
        if hit_a_wall:
            print(f"{player_one} hits a wall and needs to rest.")
            player_one_skips = True
            continue
        elif found_a_trap:
            print(f"{player_one} is out of the game! The winner is {player_two}.")
            break
        elif found_the_exit:
            print(f"{player_one} found the Exit and wins the game!")
            break


    elif counter % 2 == 0:
        if player_two_skips:
            player_two_skips = False
            counter += 1
            continue
        counter += 1
        hit_a_wall, found_the_exit, found_a_trap = player_move(row, col)
        if hit_a_wall:
            print(f"{player_two} hits a wall and needs to rest.")
            player_two_skips = True
            continue
        elif found_a_trap:
            print(f"{player_two} is out of the game! The winner is {player_one}.")
            break
        elif found_the_exit:
            print(f"{player_two} found the Exit and wins the game!")
            break
