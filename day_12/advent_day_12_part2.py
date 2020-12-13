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


def turn_ship(amount, direction, ship_ew, ship_ns):

    if direction == 'L':
        for _ in range(amount//90):
            ship_ew, ship_ns = -ship_ns, ship_ew
    else:
        for _ in range(amount // 90):
            ship_ew, ship_ns = ship_ns, -ship_ew
    return ship_ew, ship_ns







def move_ship(instructions):
    total_ew,total_ns = 0,0
    ship_ew, ship_ns = 10, 1
    for step in instructions:
        direction, amount = _parse_instructions(step)
        if direction in ['L', 'R']:
            ship_ew, ship_ns = turn_ship(amount, direction, ship_ew, ship_ns)
        if direction == 'N':
             ship_ns += amount
        if direction == 'E':
            ship_ew += amount
        if direction == 'S':
            ship_ns -= amount
        if direction == 'W':
            ship_ew -= amount
        elif direction == 'F':
            total_ew += (ship_ew * amount)
            total_ns += (ship_ns * amount)
    print (abs(total_ns) + abs(total_ew))






instructions = generate_instructions()
move_ship(instructions)
