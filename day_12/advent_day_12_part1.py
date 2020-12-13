import fileinput
import re

COMPASS = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}

def generate_instructions():
    instructions = []
    for line in fileinput.input():
        instructions.append(line.strip('\n'))
    return instructions


def _parse_instructions(instruction):
    match = re.fullmatch(r'(F|W|S|N|E|R|L)([0-9]+)', instruction)
    direction = match.group(1)
    amount = int(match.group(2))
    return direction, amount


def turn_ship(amount, direction, ship_direction):
    if direction == 'L':
        ship_direction = (ship_direction - amount) %360
    else:
        ship_direction = (ship_direction + amount) %360
    return ship_direction


def find_direction_move(ship_direction, amount, manhattan_distance):
    direction = COMPASS[ship_direction]
    manhattan_distance[direction] += amount
    return manhattan_distance

def move_ship(instructions):
    ship_direction = 90
    manhattan_distance = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    for step in instructions:
        direction, amount = _parse_instructions(step)
        if direction in ['L', 'R']:
            ship_direction = turn_ship(amount, direction, ship_direction)
        if direction in ['N', 'W', 'E', 'S']:
             manhattan_distance[direction] += amount
        if direction in ['F']:
            manhattan_distance = find_direction_move(ship_direction, amount, manhattan_distance)
    north_sourth = abs((manhattan_distance['N'] - manhattan_distance['S']))
    east_west = abs((manhattan_distance['E'] - manhattan_distance['W']))
    print (north_sourth + east_west)






instructions = generate_instructions()
move_ship(instructions)
