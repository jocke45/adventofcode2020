def row_finder(boarding_pass, row_list):
    """
    Find the correct row by recursing through a boarding pass' string
    use the top half of the rows for F and bottom half for B
    """
    if len(row_list) == 1:
        row = row_list[0]
    elif boarding_pass[0] == 'F':
        row = row_finder(boarding_pass[1:], row_list[:len(row_list)//2])
    elif boarding_pass[0] == 'B':
        row = row_finder(boarding_pass[1:], row_list[len(row_list)//2:])
    return row


def column_finder(boarding_pass, col_list):
    """
    Find the correct column by recursing through a boarding pass' string
    use the right half of the columns for R and left half for L
    """
    if len(col_list) == 1:
        col = col_list[0]
    elif boarding_pass[0] == 'L':
        col = column_finder(boarding_pass[1:], col_list[:len(col_list)//2])
    elif boarding_pass[0] == 'R':
        col = column_finder(boarding_pass[1:], col_list[len(col_list)//2:])
    return col


def seat_finder(boarding_passes):
    """
    Find what all the seat IDs given all the boarding pass data
    """
    row_list = [*range(0, 128)]
    col_list = [*range(0, 8)]
    seats = []
    for boarding_pass in boarding_passes:
        row = row_finder(boarding_pass, row_list)
        column = column_finder(boarding_pass[-3:], col_list)
        seats.append(row * 8 + column)
    return seats


def get_my_seat(plane_seats):
    """
    Get what seat ID that is not taken by comparing the taken IDs to a range
    """
    start = plane_seats[0]
    end = plane_seats[-1]
    return set(range(start, end  + 1)).difference(plane_seats)
