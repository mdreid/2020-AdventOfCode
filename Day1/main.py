FILENAME = "input.txt"
SUM_VALUE = 2020

def readEntries(filename: str) -> list[str]:
    entries = []
    with open(filename, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            entries.append(int(line))
    return entries

def solvePart1(entries: set[int]) -> None:
    print("Part 1")
    for e in entries:
        complement = SUM_VALUE - e
        if complement in entries:
            print(f"Values: {e}, {complement}\nProduct: {e * complement}")
            return

def solvePart2(entries: set[int], entries_list: list[int]) -> None:
    print("Part 2")
    for i, e1 in enumerate(entries_list):
        for j in range(i+1, len(entries_list)):
                e2 = entries_list[j]
                complement = SUM_VALUE - e1 - e2
                if complement in entries:
                    print(f"Values: {e1}, {e2}, {complement}\nProduct: {e1 * e2 * complement}")
                    return

entries = readEntries(FILENAME)
solvePart1(set(entries))
solvePart2(set(entries), entries)
