FILENAME = "input.txt"
NUM_ROWS = 128
NUM_COLS = 8

def calculateSeatId(row: int, col: int) -> int:
    return row * 8 + col

def readLocations(filename: str) -> list[str]:
    locations = []
    with open(filename, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            locations.append(line[:-1])

    return locations

def calculateRowAndColFromLocationString(location: str) -> (int, int):
    row = recurseRowOrCol(location[:7], 0, 0, NUM_ROWS-1)
    col = recurseRowOrCol(location[7:], 0, 0, NUM_COLS-1)
    return (row, col)

def recurseRowOrCol(loc: str, idx: int, lo: int, hi: int):
    # print(f"recurseRowOrCol({loc}, {idx}, {lo}, {hi})")
    if idx == len(loc):
        return lo
    mid = ((hi - lo) // 2 ) + lo
    if loc[idx] == "F" or loc[idx] == "L":
        return recurseRowOrCol(loc, idx+1, lo, mid)
    return recurseRowOrCol(loc, idx+1, mid+1, hi)

def solvePart1() -> None:
    print("Part 1")
    max_seat_id = -1
    locations = readLocations(FILENAME)
    for loc in locations:
        row, col = calculateRowAndColFromLocationString(loc)
        # print(f"Row {row}, Col {col}")
        seat_id = calculateSeatId(row, col)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    print(f"Highest seat ID: {max_seat_id}")

def solvePart2() -> None:
    print("Part 2")
    locations = readLocations(FILENAME)
    seat_ids = []
    for loc in locations:
        row, col = calculateRowAndColFromLocationString(loc)
        seat_ids.append(calculateSeatId(row, col))
    seat_ids.sort()
    idx = 0
    while idx < len(seat_ids)-1:
        if seat_ids[idx+1] - seat_ids[idx] == 2:
            print(f"My seat ID: {seat_ids[idx] + 1}")
        idx += 1
    
solvePart1()
solvePart2()
