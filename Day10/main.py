import collections

FILENAME = "input.txt"

def readAdapters(filename: str) -> list[int]:
    adapters = []
    with open(FILENAME, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            adapters.append(int(line))
    return adapters
            
def findDifferences(adapters: list) -> collections.Counter:
    difference_counter = collections.Counter() 
    max_adapter = max(adapters)
    min_adapter = min(adapters)
    has_adapter = [False] * (max_adapter + 1)
    for a in adapters:
        has_adapter[a] = True
    difference_counter[3] += 1 # built-in adapter always 3 higher than max adapter
    current_joltage = 0
    while current_joltage < max_adapter:
        diff = 1
        while current_joltage + diff < max_adapter and not has_adapter[current_joltage + diff]:
            diff += 1
        difference_counter[diff] += 1
        current_joltage += diff
    return difference_counter

def findNumDistinctArrangements(adapters: list) -> int:
    max_adapter = max(adapters)
    min_adapter = min(adapters)
    has_adapter = [False] * (max_adapter + 1)
    for a in adapters:
        has_adapter[a] = True
    num_arrangements = [0] * (max_adapter + 1)
    # Adapters reachable from charging outlet (0 zoltage)
    for i in [1, 2, 3]:
        if has_adapter[i]:
            num_arrangements[i] = 1
    curr_adapter = min_adapter
    while curr_adapter <= max_adapter:
        if has_adapter[curr_adapter]:
            if curr_adapter - 3 > 0:
                num_arrangements[curr_adapter] += num_arrangements[curr_adapter - 3]
            if curr_adapter - 2 > 0:
                num_arrangements[curr_adapter] += num_arrangements[curr_adapter - 2]
            if curr_adapter - 1 > 0:
                num_arrangements[curr_adapter] += num_arrangements[curr_adapter - 1]
        curr_adapter += 1
    # print(num_arrangements)
    return num_arrangements[max_adapter]

def solvePart1() -> None:
    print("Part 1")
    adapters = readAdapters(FILENAME)
    differences = findDifferences(adapters)
    print(f"Differences: {differences}")
    print(f"Product of 1-jolt differences and 3-jolt differences: {differences[1] * differences[3]}")

def solvePart2() -> None:
    print("Part 2")
    adapters = readAdapters(FILENAME)
    num_distinct_arrangements = findNumDistinctArrangements(adapters)
    print(f"Number of distinct arrangements: {num_distinct_arrangements}")

solvePart1()
solvePart2()
