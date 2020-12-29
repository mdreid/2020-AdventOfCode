FILENAME = "input.txt"
REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
OPTIONAL_FIELDS = {"cid"}
DELIM = ":"

def validPassport(passport: set[str]) -> bool:
    missing_fields = REQUIRED_FIELDS - passport
    if missing_fields:
        # print(f"Passport {passport} is missing fields: {missing_fields}")
        return False
    extra_fields = passport - REQUIRED_FIELDS - OPTIONAL_FIELDS
    if extra_fields:
        print(f"Extra fields: {extra_fields}")
        return False
    return True

def strToSet(passportStr: str) -> set[str]:
    s = set()
    for line in passportStr:
        fields = line.split()
        for field in fields:
            parts = field.split(DELIM)
            s.add(parts[0])
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
                passport = strToSet(curr_lines)
                passports.append(passport)
                curr_lines = []
            else:
                curr_lines.append(line)
        if curr_lines:
            passports.append(strToSet(curr_lines))
    return passports

def solvePart1() -> None:
    passports = readPassports(FILENAME)
    valid_passport_count = 0
    for passport in passports:
        if validPassport(passport):
            valid_passport_count += 1

    print(f"Number of valid passports: {valid_passport_count}")

solvePart1()
