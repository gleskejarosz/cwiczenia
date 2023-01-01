def minBitFlips(start: int, goal: int) -> int:
    steps = 0
    start_bin = str(bin(start))[2:]
    goal_bin = str(bin(goal))[2:]

    a = len(start_bin) - len(goal_bin)
    if a > 0:
        goal_bin = a * "0" + goal_bin
    elif a < 0:
        start_bin = abs(a) * "0" + start_bin

    for idx, elem in enumerate(start_bin):
        elem_goal = goal_bin[idx]
        if elem != elem_goal:
            steps += 1

    return steps


if __name__ == '__main__':
    assert (minBitFlips(start=10, goal=7)) == 3
    assert (minBitFlips(start=3, goal=4)) == 3
