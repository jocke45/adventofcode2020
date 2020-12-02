import re

def valid_passwords(passwords):
    """
    Return the number of passwords that contain 
    between a certain number of a specific letter
    Execution time: 0.03s
    """
    password_list = [re.split("[\W]+", a) for a in passwords]
    total = 0
    for b in password_list:
        count = b[3].count(b[2])
        if count >= int(b[0]) and count <= int(b[1]):
            total = total + 1
    return total


def valid_passwords_again(passwords):
    """
    Return the number of passwords that contain 
    between a specific letter in only one of two given indexes
    Execution time: 0.03s
    """
    password_list = [re.split("[\W]+", a) for a in passwords]
    total = 0
    for b in password_list:
        if (b[3][int(b[0]) - 1] == b[2]) ^ (b[3][int(b[1]) - 1] == b[2]):
            total = total + 1
    return total
