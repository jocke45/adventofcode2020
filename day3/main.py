from toboggan_route import toboggan_routes

debug = True

file = open("./trees_list.txt")
lines = [line for line in file]
file.close()


test_lines = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"]

if __name__ == "__main__":
    #print(toboggan_routes(test_lines))
    print(toboggan_routes(lines))
