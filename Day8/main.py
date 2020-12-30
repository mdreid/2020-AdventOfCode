FILENAME = "input.txt"

def readInstructions(filename: str) -> (list[str], list[str]):
    instructions = []
    nums = []
    with open(filename, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            parts = line.split(" ")
            instructions.append(parts[0])
            nums.append(int(parts[1]))
    return instructions, nums

def solvePart1() -> None:
    instructions, nums = readInstructions(FILENAME)
    visited = [False] * len(instructions)
    idx = 0
    accumulator = 0
    while not visited[idx]:
        visited[idx] = True
        instruction = instructions[idx]
        if instruction == "nop":
            idx += 1
        elif instruction == "acc":
            accumulator += nums[idx]
            idx += 1
        else: # instruction == "jmp"
            idx += nums[idx]
    print(f"Value of accumulator at time of cycle: {accumulator}")

solvePart1()
