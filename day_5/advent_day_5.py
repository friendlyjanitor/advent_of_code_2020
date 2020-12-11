import fileinput



boarding_passes = []
for line in fileinput.input():
    seat_data = []
    seat_data.append(line[:7])
    seat_data.append(line[7:10])
    boarding_passes.append(seat_data)

    #return row_data, column_data
def find_row(row_data):
    row = 0
    row_position = 64
    for data in row_data:
        if data == 'B':
            row += row_position
        row_position /= 2
    return row

def find_column(column_data):
    col = 0
    col_position = 4
    for data in column_data:
        if data == 'R':
            col += col_position
        col_position /= 2
    return col

def find_missing_seat(seat_ids):
    return[x for x in range(seat_ids[0], seat_ids[-1] + 1) if x not in seat_ids]

def find_seat_id(boarding_passes):
    seat_ids = []
    for bp in boarding_passes:
        row = find_row(bp[0])
        column = find_column(bp[1])
        seat_id = (row * 8) + column
        seat_ids.append(seat_id)
    my_seat = find_missing_seat(sorted(seat_ids))
    print my_seat


find_seat_id(boarding_passes)
