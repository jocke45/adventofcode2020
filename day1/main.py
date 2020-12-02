from expense_report import expense_report, triple_expense_report

debug = True

file = open("./expense_report_list.txt")
lines = [int(line) for line in file]
file.close()

test_lines = [1721, 979, 366, 299, 675, 1456]

if __name__ == "__main__":
    print(expense_report(lines)) # 1018336
    print(triple_expense_report(lines)) # 288756720
    