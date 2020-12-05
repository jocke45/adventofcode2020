from seat_finder import seat_finder, column_finder, get_my_seat

data = []

with open("./boarding_pass_list.txt") as file:
    lines = file.read().splitlines()


test_lines = ["FBFBBFFRLR",
              "BFFFBBFRRR",
              "FFFBBBFRRR",
              "BBFFBBFRLL"]

if __name__ == "__main__":
    result = seat_finder(lines)
    result.sort()
    print(get_my_seat(result))
