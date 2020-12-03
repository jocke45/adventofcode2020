import numpy


def toboggan_route(geography, steps, falls=1):
    """
    Count the occurences of # while traversing the lists downward
    Execution time: 0.02s
    """
    x_pos = 0
    tree_count = 0
    for a in range(len(geography)):
        if a % falls:
            continue
        if x_pos > 30:
            x_pos = x_pos - 31
        if geography[a][x_pos] == "#":
            tree_count = tree_count + 1
        x_pos = x_pos + steps

    return tree_count


def toboggan_routes(geography):
    """
    Count the occurences of # while traversing the lists in specified steps
    Execution time: 0.22s
    """
    results = []
    results.append(toboggan_route(geography, 1))
    results.append(toboggan_route(geography, 3))
    results.append(toboggan_route(geography, 5))
    results.append(toboggan_route(geography, 7))
    results.append(toboggan_route(geography, 1, 2))
    return numpy.prod(results)
