FILENAME = "input.txt"
LINE_DELIMITER = " "
RANGE_DELIMITER = "-"

class Policy(object):
    lo = 0
    hi = 0
    letter = ''

    def __init__(self, lo:int, hi:int, letter:str):
        self.lo = lo
        self.hi = hi
        self.letter = letter

    def isValidLegacyPassword(self, password:str)->bool:
        count = 0
        for c in password:
            if c == self.letter:
                count += 1

        return count >= self.lo and count <= self.hi

    def isValidPositionalPassword(self, password:str)->bool:
        # Note: indices are 1-based
        return xor(password[self.lo - 1] == self.letter, password[self.hi - 1] == self.letter) 

    def __str__(self):
        return f"lo: {self.lo}, hi: {self.hi}, letter: {self.letter}"

def xor(b1: bool, b2: bool)->bool:
    return b1 != b2

def parsePolicyAndPassword(line: str)->(Policy, str):
    parts = line.split(LINE_DELIMITER)
    char_range = parts[0].split(RANGE_DELIMITER)
    lo = int(char_range[0])
    hi = int(char_range[1])
    letter = parts[1][0]
    password = parts[2]
    return Policy(lo, hi, letter), password

def readPoliciesAndPasswords(filename: str)->(list[Policy], list[str]):
    policies = []
    passwords = []
    with open(FILENAME, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            policy, password = parsePolicyAndPassword(line)
            # print(policy)
            policies.append(policy)
            passwords.append(password)

    return policies, passwords

def solvePart1()->None:
    print("Part 1")
    policies, passwords = readPoliciesAndPasswords(FILENAME)

    valid_password_count = 0
    for policy, password in zip(policies, passwords):
        if policy.isValidLegacyPassword(password):
            # print(f"Legacy password {password} is valid on policy {policy}")
            valid_password_count += 1

    print(f"Valid legacy passwords: {valid_password_count}")

def solvePart2()->None:
    print("Part 2")
    policies, passwords = readPoliciesAndPasswords(FILENAME)

    valid_password_count = 0
    for policy, password in zip(policies, passwords):
        if policy.isValidPositionalPassword(password):
            # print(f"Positional password {password} is valid on policy {policy}")
            valid_password_count += 1

    print(f"Valid positional passwords: {valid_password_count}")

solvePart1()
solvePart2()
