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

class Node:
    def __init__(self, index):
        self.next = None
        self.prev = None
        self.fro = []
        self.to = None
        self.index = index

    def __str__(self):
        return_str = f"Index: {self.index}|"
        if self.next:
            return_str += f"Next: {self.next.index}|"
        if self.prev:
            return_str += f"Prev: {self.prev.index}|"
        if self.fro:
            return_str += f"From: {self.fro.index}|"
        if self.to:
            return_str += f"To: {self.to.index}|"
        return return_str+"\n"

def buildNodeListFromInstructions(instructions: list[str], offsets: list[int]) -> list[Node]:
    num_instr = len(instructions)
    node_list = [Node(i) for i in range(num_instr+1)] # +1 for node after end of file
    idx = 0
    while idx < num_instr:
        curr = node_list[idx]
        instruction = instructions[idx]
        offset = offsets[idx]
        if instruction == "acc" or instruction == "nop":
            if idx + 1 < num_instr + 1:
                curr.next = node_list[idx+1]
                node_list[idx+1].prev = curr
        else: # instruction == "jmp"
            if idx + offset < num_instr + 1 and idx + offset >= 0:
                curr.to = node_list[idx + offset] 
                node_list[idx + offset].fro.append(curr)
        idx += 1
    return node_list

def findInstructionsReachableFromEnd(node_list: list[Node], reachable: list[bool], curr: Node) -> None:
    if reachable[curr.index]:
        return
    reachable[curr.index] = True
    if curr.prev:
        findInstructionsReachableFromEnd(node_list, reachable, curr.prev)
    for node in curr.fro:
        findInstructionsReachableFromEnd(node_list, reachable, node)
    

def containsCycle(instructions: list[str], nums: list[int]):
    visited = [False] * len(instructions)
    idx = 0
    accumulator = 0
    while idx < len(instructions) and not visited[idx]:
        visited[idx] = True
        instruction = instructions[idx]
        if instruction == "nop":
            idx += 1
        elif instruction == "acc":
            accumulator += nums[idx]
            idx += 1
        else: # instruction == "jmp"
            idx += nums[idx]

    if idx == len(instructions):
        return False, accumulator
    return True, accumulator
   

def solvePart1() -> None:
    print("Part 1")
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

def solvePart2() -> None:
    print("Part 2")
    instructions, nums = readInstructions(FILENAME)
    node_list = buildNodeListFromInstructions(instructions, nums)
    reachable_from_end = [False] * len(node_list)
    findInstructionsReachableFromEnd(node_list, reachable_from_end, node_list[-1])
    instructions, nums = readInstructions(FILENAME)

    line_number = 0
    accumulator = 0
    switch_used = False
    while line_number < len(instructions):
        instr = instructions[line_number]
        val = nums[line_number]
        if instr == "acc":
            accumulator += val
            line_number += 1
        elif instr == "nop":
            if (not switch_used) and ((line_number + val) >= 0) and ((line_number + val) < len(instructions)) and reachable_from_end[line_number + val]:
                print(f"Switched the nop on line {line_number} to jmp (has offset {val})")
                switch_used = True
                line_number += val
            else:
                line_number += 1
        elif instr == "jmp":
            if (not switch_used) and ((line_number + 1) < len(instructions)) and reachable_from_end[line_number + 1]:
                print(f"Switched the jmp (has offset {val}) on line {line_number} to nop)")
                switch_used = True
                line_number += 1
            else:
                line_number += val
    print(f"Value of accumulator after program terminates: {accumulator}")

solvePart1()
solvePart2()
