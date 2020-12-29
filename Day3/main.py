FILENAME = "input.txt"
TREE_MARKER = "#"

def readForest(filename: str) -> list[str]:
    tree_positions = []
    with open(FILENAME, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            tree_positions.append(line[:-1]) # ignore \n
    return tree_positions

def countTreesForSlope(forest: list[str], right: int, down: int) -> int:
    tree_count = 0
    pos = 0
    for i in range(0, len(forest), down):
        line = forest[i]
        if line[pos] == TREE_MARKER:
            tree_count += 1
        pos = (pos + right) % (len(line))
    return tree_count

def solvePart1() -> None:
    print("Part 1")
    forest = readForest(FILENAME)
    tree_count = countTreesForSlope(forest, 3, 1)
    print(f"Tree count: {tree_count}")

def solvePart2() -> None:
    print("Part 2")
    forest = readForest(FILENAME)
    tree_count_1r_1d = countTreesForSlope(forest, 1, 1)
    tree_count_3r_1d = countTreesForSlope(forest, 3, 1)
    tree_count_5r_1d = countTreesForSlope(forest, 5, 1)
    tree_count_7r_1d = countTreesForSlope(forest, 7, 1)
    tree_count_1r_2d = countTreesForSlope(forest, 1, 2)
    print(f"(1R, 1D): {tree_count_1r_1d}, (3R, 1D): {tree_count_3r_1d}, (5R, 1D): {tree_count_5r_1d}, (7R, 1D): {tree_count_7r_1d}, (1R, 2D): {tree_count_1r_2d}\nMultiplied: {tree_count_1r_1d * tree_count_3r_1d * tree_count_5r_1d * tree_count_7r_1d * tree_count_1r_2d}")

solvePart1()
solvePart2()
