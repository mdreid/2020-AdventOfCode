import collections

FILENAME = "input.txt"
PREAMBLE_SIZE = 25
TARGET_NUMBER = 1492208709

current_sums = collections.Counter()
current_values = []

def populateInitialSums(fp) -> list[list]:
    sums = [[-1 for i in range(PREAMBLE_SIZE)] for j in range(PREAMBLE_SIZE)]
    for i in range(PREAMBLE_SIZE):
        current_values.append(int(fp.readline()))
    for i in range(PREAMBLE_SIZE):
        for j in range(PREAMBLE_SIZE):
            if i == j:
                continue
            total = current_values[i] + current_values[j]
            sums[i][j] = total
            current_sums[total] += 1 # note: we are double counting
    return sums

def findInvalidNumber(filename: str) -> int:
    with open(filename) as fp:
        sums = populateInitialSums(fp)
        index = 0
        while True:
            line = fp.readline()
            if not line:
                break
            new_val = int(line)
            if current_sums[new_val] == 0:
                return new_val
            # we're making a row and a column, starting at index for this
            old_val = current_values[index]
            current_values[index] = new_val
            diff = new_val - old_val
            for i in range(PREAMBLE_SIZE):
                if i == index:
                    continue
                old_sum = sums[index][i]
                new_sum = old_sum + diff
                sums[index][i] = new_sum
                sums[i][index] = new_sum
                current_sums[new_sum] += 2
                current_sums[old_sum] -= 2

            index = (index + 1) % PREAMBLE_SIZE

def findRange(filename: str, target: int) -> list[int]:
    curr_sum = 0
    current_numbers = collections.deque()
    with open(filename) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            val = int(line)
            if curr_sum < target:
                curr_sum += val
                current_numbers.append(val)
            while curr_sum > target:
                curr_sum -= current_numbers.popleft()
            if curr_sum == target:
                return list(current_numbers)

def solvePart1() -> None:
    print("Part 1")
    print(findInvalidNumber(FILENAME))

def solvePart2() -> None:
    print("Part 2")
    contiguous_range = findRange(FILENAME, TARGET_NUMBER)
    print(contiguous_range)
    min_val = min(contiguous_range)
    max_val = max(contiguous_range)
    total = min_val + max_val
    print(f"Min: {min_val}, Max: {max_val}, Total: {min_val + max_val}")

solvePart1()
solvePart2()
