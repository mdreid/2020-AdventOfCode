FILENAME = "input.txt"

def findFinalPositionPart1(filename: str) -> dict[str, int]:
    positions = {'ew': 0, 'ns': 0}
    current_direction = "E"
    with open(filename, "r") as fp:
        while True:
            # print(positions)
            line = fp.readline()
            if not line:
                break
            action = line[0]
            val = int(line[1:])
            "E and N will be positive"
            if action in "EWNS":
                updatePositions(action, positions, val)
            elif action == "F":
                updatePositions(current_direction, positions, val)
            elif action == "R":
                current_direction = rotateRight(current_direction, val)
            else: # action == "L":
                current_direction = rotateLeft(current_direction, val)
        return positions

def findFinalPositionPart2(filename: str) -> dict[str, int]:
    positions = {'ew': 0, 'ns': 0}
    waypt_positions = {'ew': 10, 'ns': 1}
    with open(filename, "r") as fp:
        while True:
            # print(positions)
            line = fp.readline()
            if not line:
                break
            action = line[0]
            val = int(line[1:])
            "E and N will be positive"
            if action in "EWNS":
                updatePositions(action, waypt_positions, val)
            elif action == "F":
                ew_change = val * waypt_positions["ew"]
                ns_change = val * waypt_positions["ns"]
                positions["ew"] += ew_change
                positions["ns"] += ns_change
            elif action == "R":
                current_direction = rotateWaypointRight(waypt_positions, val)
            else: # action == "L":
                current_direction = rotateWaypointLeft(waypt_positions, val)
        return positions

def rotateRight(direction: str, degrees: int) -> str:
    while degrees > 0:
        if direction == "N":
            direction = "E"
        elif direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        elif direction == "W":
            direction = "N"
        degrees -= 90
    return direction

def rotateLeft(direction: str, degrees: int) -> str:
    return rotateRight(direction, 360-degrees)

def rotateWaypointRight(positions: dict[str, int], degrees: int) -> None:
    while degrees > 0:
        ew = positions["ew"]
        ns = positions["ns"]
        positions["ew"] = ns
        positions["ns"] = -1 * ew
        """
        if ew == 0:
            positions["ew"] = ns
            positions["ns"] = 0
        elif ns == 0:
            positions["ew"] = 0
            positions["ns"] = ew
        elif ew > 0 and ns > 0: # Quadrant I
            positions["ew"] = ns
            positions["ns"] = -1 * ew
        elif ew > 0 and ns < 0: # Quadrant IV
            positions["ew"] = ns
            positions["ns"] = -1 * ew
        elif ew < 0 and ns < 0: # Quadrant III
            positions["ew"] = ns
            positions["ns"] = -1 * ew
        elif ew > 0 and ns > 0: # Quadrant II
            positions["ew"] = ns
            positions["ns"] = -1 * ew
        """
        degrees -= 90

def rotateWaypointLeft(positions: dict[str, int], degrees: int) -> None:
    return rotateWaypointRight(positions, 360-degrees)

def updatePositions(direction: str, positions: dict[str, int], val: int) -> None:
    if direction == "E":
        positions["ew"] += val
    elif direction == "W":
        positions["ew"] -= val
    elif direction == "N":
        positions["ns"] += val
    elif direction == "S":
        positions["ns"] -= val

def solvePart1() -> None:
    print("Part 1")
    position = findFinalPositionPart1(FILENAME)
    print(f"EW: {position['ew']}, NS: {position['ns']}")
    manhattan_dist = abs(position["ew"]) + abs(position["ns"])
    print(f"Manhattan distance: {manhattan_dist}")

def solvePart2() -> None:
    print("Part 2")
    position = findFinalPositionPart2(FILENAME)
    print(f"EW: {position['ew']}, NS: {position['ns']}")
    manhattan_dist = abs(position["ew"]) + abs(position["ns"])
    print(f"Manhattan distance: {manhattan_dist}")

solvePart1()
solvePart2()
