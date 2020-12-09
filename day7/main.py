from bag_puzzle import bag_puzzle


with open("./bags_sample.txt") as file:
    lines = file.read().splitlines()


if __name__ == "__main__":
    bag_puzzle(lines)
