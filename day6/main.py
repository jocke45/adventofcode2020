from custom_checker import count_answers, common_answers
import numpy


def part_one():
    """
    Format the input data so that it is easy to use for part one
    """
    with open("./question_answers.txt") as file:
        return map(lambda x: numpy.array(list(x.replace("\n", ""))),
                   file.read().split("\n\n"))


def part_two():
    """
    Format the input data so that it is easy to use for part two
    """
    with open("./question_answers.txt") as file:
        return map(lambda x: x.split("\n"), [a for a in file.read().split("\n\n")])


if __name__ == "__main__":
    print(count_answers(part_one()))
    print(common_answers(part_two()))
