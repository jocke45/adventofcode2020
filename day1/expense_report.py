def expense_report(report, debug=False):
    """
    Return the product of two integers that together add to 2020
    Execution time: 0,02s
    """
    report.sort(reverse=True)
    for x in report:
        for y in range(len(report) - 1, 0, -1):
            # Iterate backwards. Since the list is sorted we might
            # be able to cut a lot of list entries this way
            if x + report[y] == 2020:
                return x * report[y]
            elif x + report[y] > 2020:
                break  # The sum will be to big for the rest of the list


def triple_expense_report(report, debug=False):
    """
    Return the product of three integers that together add to 2020
    Execution time: 0,04s
    Execution time w/o "backwards break" trick: 0,52s
    """
    report.sort(reverse=True)
    for x in range(0, len(report), 1):
        for y in range(x + 1, len(report), 1):
            for z in range(len(report) - 1, 0, -1):
                # Iterate backwards. Since the list is sorted we might
                # be able to cut a lot of list entries this way
                if report[x] + report[y] + report[z] == 2020:
                    return report[x] * report[y] * report[z]
                elif report[x] + report[y] + report[z] > 2020:
                    break  # The sum will be to big for the rest of the list
