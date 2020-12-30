import collections

FILENAME = "input.txt"

def readFileIntoDataStructurePart1(filename: str) -> dict[str, list[str]]:
    # dictionary["style color"] = list of style colors that contain it
    colors_to_colors_that_contain_it = collections.defaultdict(list)
    with open(filename, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            color, contained_colors = parseLinePart1(line)
            for c in contained_colors:
                colors_to_colors_that_contain_it[c].append(color)
    return colors_to_colors_that_contain_it

def readFileIntoDataStructurePart2(filename: str) -> dict[str, list]:
    # dictionary["style color"] = list of (style color, count) that it contains
    colors_to_contained_colors = collections.defaultdict(list)
    with open(filename, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            color, contained_colors = parseLinePart2(line)
            for color_count_tuple in contained_colors:
                # print(color_count_tuple)
                colors_to_contained_colors[color].append(color_count_tuple)
    return colors_to_contained_colors

def parseLinePart1(line: str) -> (str, list[str]):
    parts = line.split("bag")
    color = parts[0].strip()
    if "no other" in line:
        return color, []

    contained_colors = []
    remainder = line.split(" ")[4:]
    idx = 0
    while idx < len(remainder):
        contained_colors.append(remainder[idx+1] + " " + remainder[idx+2])
        idx += 4
    return color, contained_colors

def parseLinePart2(line: str) -> (str, list[str]):
    parts = line.split("bag")
    color = parts[0].strip()
    if "no other" in line:
        return color, []

    contained_colors = []
    remainder = line.split(" ")[4:]
    idx = 0
    # print(line)
    while idx < len(remainder):
        contained_color = remainder[idx+1] + " " + remainder[idx+2]
        count = int(remainder[idx])
        # print(remainder)
        # print(count)
        contained_colors.append((contained_color, count))
        idx += 4
    return color, contained_colors

def countNumUniqueBagsForColor(colors_to_colors_that_contain_it: dict[str, list[str]], visited: dict[str, bool], color: str) -> int:
    if visited[color]:
        return 0
    visited[color] = True
    count = 1
    for c in colors_to_colors_that_contain_it[color]:
        count += countNumUniqueBagsForColor(colors_to_colors_that_contain_it, visited, c)
    return count

def solvePart1() -> None:
    colors_to_colors_that_contain_it = readFileIntoDataStructurePart1(FILENAME)
    visited = collections.defaultdict(bool)
    num_shiny_gold_bags = countNumUniqueBagsForColor(colors_to_colors_that_contain_it, visited, "shiny gold") - 1
    print(f"Number of bag colors that can eventually contain at least one shiny gold bag: {num_shiny_gold_bags}")

def countTotalBagsForColor(colors_to_contained_colors: dict[str, list], color: str) -> int:
    count = 1
    for contained_color, contained_color_count in colors_to_contained_colors[color]:
        count += contained_color_count * countTotalBagsForColor(colors_to_contained_colors, contained_color)
    return count

def solvePart2() -> None:
    colors_to_contained_colors = readFileIntoDataStructurePart2(FILENAME)
    num_shiny_gold_bags = countTotalBagsForColor(colors_to_contained_colors, "shiny gold") - 1
    print(f"Number of bags contained by one shiny gold bag: {num_shiny_gold_bags}")

solvePart1()
solvePart2()
