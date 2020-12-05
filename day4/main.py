from passport_validator import passport_validator, passport_data_validator

data = []

with open("./passport_list.txt") as file:
    for a in file.read().split("\n\n"):
        data.append(dict(c.split(":")
                         for c in a.replace("\n", " ").split(" ")))


if __name__ == "__main__":
    print(passport_validator(data))