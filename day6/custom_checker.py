import numpy


def count_answers(answers):
    """
    Return the number of unique answers in the input
    """
    count = 0
    for answer in answers:
        count = count + len(numpy.unique(answer))
    return count


def common_answers(answers):
    """
    Return the intersection of the input
    """
    count = 0
    for answer in answers:
        count = count + len(list(set.intersection(*(map(set, answer)))))
    return count
