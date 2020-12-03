from valid_passwords import valid_passwords, valid_passwords_again

debug = True

file = open("./password_list.txt")
lines = [line for line in file]
file.close()

test_lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

if __name__ == "__main__":
    print(valid_passwords(lines))
    print(valid_passwords_again(lines))
