import fileinput
import numpy as np
from copy import deepcopy



def generate_seat_matrix():
    seat_matrix = []
    for line in fileinput.input():
        seat_matrix.append(list(line.strip('\n')))
    return seat_matrix


def find_neighbors(seat_matrix, seat_row, seat):
    filled_count = 0
    for seat_row_change in [-1, 0, 1]:
        for seat_column_change in [-1, 0, 1]:
            checking_seat_row = seat_row + seat_row_change
            checking_seat_column = seat + seat_column_change
            if checking_seat_column == seat and checking_seat_row == seat_row:
                continue
            try:
                if 0 <= checking_seat_row < len(seat_matrix) and 0 <= checking_seat_column < len(seat_matrix[checking_seat_row]) and seat_matrix[checking_seat_row][checking_seat_column] == '#':
                    filled_count += 1
            except IndexError:
                continue
    return filled_count

def change_seat(copied_seats, seat_row, seat, neighbor_count):
    if copied_seats[seat_row][seat] == 'L' and neighbor_count == 0:
        copied_seats[seat_row][seat] = '#'
    elif neighbor_count >= 4:
        copied_seats[seat_row][seat] = 'L'


def change_round(seat_matrix):
    copied_seats = deepcopy(seat_matrix)
    for seat_row in range(len(seat_matrix)):
        for seat in range(len(seat_matrix[seat_row])):
            if seat_matrix[seat_row][seat] == '.':
                continue
            neighbor_count = find_neighbors(seat_matrix, seat_row, seat)
            change_seat(copied_seats, seat_row, seat, neighbor_count)
    return copied_seats

def count(seat_matrix):
    total = 0
    for row in seat_matrix:
        total += row.count('#')
    return total

def run_through_rules(seat_matrix):
    after_round = change_round(seat_matrix)
    while after_round != seat_matrix:
        seat_matrix = deepcopy(after_round)
        after_round = change_round(seat_matrix)
    print (count(seat_matrix))


seat_matrix = generate_seat_matrix()
run_through_rules(seat_matrix)