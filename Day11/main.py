import copy
from typing import Callable

FILENAME = "input.txt"

def readSeatingChart(filename: str) -> list[list[str]]:
    seats = []
    with open(filename, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            seats.append([char for char in line if char in ['.', '#', 'L']])
    return seats


def calculateNewSeatPart1(seats: list[list[str]], i: int, j: int) -> str:
    if seats[i][j] == ".":
        return "."
    if seats[i][j] == "L":
        if countAdjacentOccupiedSeats(seats, i, j) == 0:
            return "#"
        return "L"
    # seats[i][j] == "#"
    if countAdjacentOccupiedSeats(seats, i, j) >= 4:
        return "L"
    return "#"

def calculateNewSeatPart2(seats: list[list[str]], i: int, j: int) -> str:
    if seats[i][j] == ".":
        return "."
    if seats[i][j] == "L":
        if countVisibleOccupiedSeats(seats, i, j) == 0:
            return "#"
        return "L"
    # seats[i][j] == "#"
    if countVisibleOccupiedSeats(seats, i, j) >= 5:
        return "L"
    return "#"

def isOccupied(seats: list[list[str]], i: int, j: int) -> int:
    if i < 0 or i > len(seats) - 1:
        return 0
    if j < 0 or j > len(seats[i]) - 1:
        return 0
    return seats[i][j] == "#"

def countAdjacentOccupiedSeats(seats: list[list[str]], i: int, j: int) -> int:
    count = 0
    count += isOccupied(seats, i+1, j)
    count += isOccupied(seats, i-1, j)
    count += isOccupied(seats, i, j+1)
    count += isOccupied(seats, i, j-1)
    count += isOccupied(seats, i+1, j+1)
    count += isOccupied(seats, i+1, j-1)
    count += isOccupied(seats, i-1, j+1)
    count += isOccupied(seats, i-1, j-1)
    return count

def countVisibleOccupiedSeats(seats: list[list[str]], i: int, j: int) -> int:
    count = 0
    idx_i = i + 1
    while idx_i < len(seats):
        if seats[idx_i][j] == "#":
            count += 1
            break
        elif seats[idx_i][j] == "L":
            break
        idx_i += 1
    idx_i = i - 1
    while idx_i >= 0:
        if seats[idx_i][j] == "#":
            count += 1
            break
        elif seats[idx_i][j] == "L":
            break
        idx_i -= 1
    idx_j = j + 1
    while idx_j < len(seats[i]):
        if seats[i][idx_j] == "#":
            count += 1
            break
        elif seats[i][idx_j] == "L":
            break
        idx_j += 1
    idx_j = j - 1
    while idx_j >= 0:
        if seats[i][idx_j] == "#":
            count += 1
            break
        elif seats[i][idx_j] == "L":
            break
        idx_j -= 1
    idx_i = i + 1
    idx_j = j + 1
    while idx_i < len(seats) and idx_j < len(seats[i]):
        if seats[idx_i][idx_j] == "#":
            count += 1
            break
        elif seats[idx_i][idx_j] == "L":
            break
        idx_i += 1
        idx_j += 1
    idx_i = i + 1
    idx_j = j - 1
    while idx_i < len(seats) and idx_j >= 0:
        if seats[idx_i][idx_j] == "#":
            count += 1
            break
        elif seats[idx_i][idx_j] == "L":
            break
        idx_i += 1
        idx_j -= 1
    idx_i = i - 1
    idx_j = j + 1
    while idx_i >= 0 and idx_j < len(seats[i]):
        if seats[idx_i][idx_j] == "#":
            count += 1
            break
        elif seats[idx_i][idx_j] == "L":
            break
        idx_i -= 1
        idx_j += 1
    idx_i = i - 1
    idx_j = j - 1
    while idx_i >= 0 and idx_j >= 0:
        if seats[idx_i][idx_j] == "#":
            count += 1
            break
        elif seats[idx_i][idx_j] == "L":
            break
        idx_i -= 1
        idx_j -= 1
    return count


def simulateUntilStasis(seats: list[list[str]], newSeatCalculator: Callable[[list[list[str]], int, int], str]) -> list[list[str]]:
    prev_seats = seats
    curr_seats = copy.deepcopy(prev_seats)
    has_changes = True
    while has_changes:
        has_changes = False
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                curr_seat = prev_seats[i][j]
                calculated_seat = newSeatCalculator(prev_seats, i, j)
                if curr_seat != calculated_seat:
                    has_changes = True
                    curr_seats[i][j] = calculated_seat
        prev_seats = copy.deepcopy(curr_seats)
    return curr_seats

def countOccupiedSeats(seats: list[list[str]]) -> int:
    occupied_count = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                occupied_count += 1
    return occupied_count

def solvePart1() -> None:
    print("Part 1")
    seats = readSeatingChart(FILENAME)
    equilibrium_seats = simulateUntilStasis(seats, calculateNewSeatPart1)
    occupied_seats = countOccupiedSeats(equilibrium_seats)
    print(f"Occupied seats: {occupied_seats}")

def solvePart2() -> None:
    print("Part 2")
    seats = readSeatingChart(FILENAME)
    equilibrium_seats = simulateUntilStasis(seats, calculateNewSeatPart2)
    occupied_seats = countOccupiedSeats(equilibrium_seats)
    print(f"Occupied seats: {occupied_seats}")

solvePart1()
solvePart2()
