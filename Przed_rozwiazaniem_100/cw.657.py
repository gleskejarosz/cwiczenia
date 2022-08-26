def judgeCircle(moves: str) -> bool:
    move_dict = {"R": 1, "L": -1, "U": 1, "D": -1}
    start = [0, 0]

    for move in moves:
        if move == "R" or move == "L":
            start[0] += move_dict[move]
        else:
            start[1] += move_dict[move]

    if start == [0, 0]:
        return True
    else:
        return False


if __name__ == '__main__':
    assert(judgeCircle("UD")) is True
    assert(judgeCircle("LL")) is False
