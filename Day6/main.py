FILENAME = "input.txt"

def readGroupAnswers(filename: str) -> list[list[str]]:
    with open(filename, "r") as fp:
        group_answers = []
        curr_group_answers = []
        while True:
            line = fp.readline()
            if not line:
                break
            if line == "\n":
                group_answers.append(curr_group_answers)
                curr_group_answers = []
            else:
                curr_group_answers.append(line[:-1])
        if curr_group_answers:
            group_answers.append(curr_group_answers)
    return group_answers

def countDistinctAnswers(group_answers) -> int:
    answer_str = "".join(group_answers)
    return len(set(answer_str))

def countAnswersSharedByGroup(group_answers) -> int:
    letter_counts = [0] * 26
    num_group_members = len(group_answers)
    for person_answers in group_answers:
        for a in person_answers:
            letter_counts[ord(a) - ord('a')] += 1
    shared_by_all = 0
    for cnt in letter_counts:
        if cnt == num_group_members:
            shared_by_all += 1
    return shared_by_all
    
def solveProblem1() -> None:
    group_answers = readGroupAnswers(FILENAME)
    sum_counts = 0
    for group in group_answers:
        sum_counts += countDistinctAnswers(group)
    print(f"Sum of counts: {sum_counts}")

def solveProblem2() -> None:
    group_answers = readGroupAnswers(FILENAME)
    sum_counts = 0
    for group in group_answers:
        sum_counts += countAnswersSharedByGroup(group)
    print(f"Sum of counts: {sum_counts}")

solveProblem1()
solveProblem2()
