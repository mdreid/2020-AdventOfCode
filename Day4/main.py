import re

FILENAME = "input.txt"
REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
OPTIONAL_FIELDS = {"cid"}
DELIM = ":"
VALID_EYE_COLORS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
PASSPORT_ID_PATTERN = re.compile("\d{9}")
HAIR_COLOR_PATTERN = re.compile("#[0-9a-f]{6}")

def passportContainsCorrectFields(passport: dict[str, str]) -> bool:
    keys = set(passport.keys())
    missing_fields = REQUIRED_FIELDS - keys
    if missing_fields:
        # print(f"Passport {passport} is missing fields: {missing_fields}")
        return False
    extra_fields = keys - REQUIRED_FIELDS - OPTIONAL_FIELDS
    if extra_fields:
        print(f"Extra fields: {extra_fields}")
        return False
    return True

def validBirthYear(year: str) -> bool:
    return len(year) == 4 and int(year) >= 1920 and int(year) <= 2002

def validIssueYear(year: str) -> bool:
    return len(year) == 4 and int(year) >= 2010 and int(year) <= 2020

def validExpirationYear(year: str) -> bool:
    return len(year) == 4 and int(year) >= 2020 and int(year) <= 2030

def validHeight(height: str) -> bool:
    if len(height) < 3:
        return False
    unit = height[-2:]
    value = int(height[:-2])
    if unit == "cm":
        return value >= 150 and value <= 193
    if unit == "in":
        return value >= 59 and value <= 76
    return False

def validHairColor(color: str) -> bool:
    return HAIR_COLOR_PATTERN.fullmatch(color)

def validEyeColor(color: str) -> bool:
    return color in VALID_EYE_COLORS

def validPassportId(pid: str) -> bool:
    return PASSPORT_ID_PATTERN.fullmatch(pid)

def validPassport(passport: dict[str, str]) -> bool:
    if not passportContainsCorrectFields(passport):
        return False
    if not validBirthYear(passport["byr"]):
        return False
    if not validIssueYear(passport["iyr"]):
        return False
    if not validExpirationYear(passport["eyr"]):
        return False
    if not validHeight(passport["hgt"]):
        return False
    if not validHairColor(passport["hcl"]):
        return False
    if not validEyeColor(passport["ecl"]):
        return False
    if not validPassportId(passport["pid"]):
        return False
    return True

def strToDict(passportStr: str) -> dict[str, str]:
    s = dict()
    for line in passportStr:
        fields = line.split()
        for field in fields:
            parts = field.split(DELIM)
            s[parts[0]] = parts[1]
    return s

def readPassports(filename: str) -> list[list]:
    passports = []
    with open(FILENAME, "r") as fp:
        curr_lines = []
        while True:
            line = fp.readline()
            if not line:
                break
            if line == '\n': 
                passport = strToDict(curr_lines)
                passports.append(passport)
                curr_lines = []
            else:
                curr_lines.append(line)
        if curr_lines:
            passports.append(strToDict(curr_lines))
    return passports

def solvePart1() -> None:
    print("Part 1")
    passports = readPassports(FILENAME)
    valid_passport_count = 0
    for passport in passports:
        if passportContainsCorrectFields(passport):
            valid_passport_count += 1

    print(f"Number of valid passports: {valid_passport_count}")

def solvePart2() -> None:
    print("Part 2")
    passports = readPassports(FILENAME)
    valid_passport_count = 0
    for passport in passports:
        if validPassport(passport):
            valid_passport_count += 1

    print(f"Number of valid passports: {valid_passport_count}")

solvePart1()
solvePart2()
