import re


def passport_validator(passports):
    """
    How many dictionaries contains all keys but "cid"
    """
    count = 0
    for passport in passports:
        if not "ecl" in passport:
            continue
        if not "pid" in passport:
            continue
        if not "eyr" in passport:
            continue
        if not "hcl" in passport:
            continue
        if not "byr" in passport:
            continue
        if not "iyr" in passport:
            continue
        if not "hgt" in passport:
            continue
        if passport_data_validator(passport):
            count = count + 1
    return count


def passport_data_validator(passport):
    """
    Validating the data in passports that have the required 
    """
    if not (len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2020):
        return False
    if not (len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (len(passport['eyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030):
        return False
    len_unit = passport['hgt'][-2::1]
    try:
        height = int(passport['hgt'][:-2:1])
    except:
        return False
    if len_unit not in ["cm", "in"]:
        return False
    elif len_unit == 'cm' and ( 193 < height or height < 150):
        return False
    elif len_unit == 'in' and 76 < height or height < 59:
        return False
    if not re.match("^#[a-f0-9]{6}$", passport['hcl']):
        return False
    if passport['ecl'] not in ["amb", "blu", "brn", "gry", "grn", "hzl","oth"]:
        return False
    if not re.match("^[0-9]{9}$", passport['pid']):
        return False
    return True
