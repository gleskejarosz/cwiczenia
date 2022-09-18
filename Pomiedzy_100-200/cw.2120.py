def executeInstructionsn(n: int, startPos: list, s: str) -> list:
    vertical_vector = startPos[0]
    horizontal_vector = startPos[1]
    result = []
    moves = 0
    loop = 0

    while len(s) - loop > 0:
        s_array = s[loop:]
        for elem in s_array:
            if elem == "R":
                horizontal_vector += 1
                if horizontal_vector > n - 1:
                    result.append(moves)
                    break
                moves += 1
            if elem == "L":
                horizontal_vector -= 1
                if horizontal_vector < 0:
                    result.append(moves)
                    break
                moves += 1
            if elem == "D":
                vertical_vector += 1
                if vertical_vector > n - 1:
                    result.append(moves)
                    break
                moves += 1
            if elem == "U":
                vertical_vector -= 1
                if vertical_vector < 0:
                    result.append(moves)
                    break
                moves += 1
        loop += 1
        if loop > len(result):
            result.append(moves)
        moves = 0
        vertical_vector = startPos[0]
        horizontal_vector = startPos[1]

    return result


if __name__ == '__main__':
    assert (executeInstructionsn(n=3, startPos=[0, 1], s="RRDDLU")) == [1, 5, 4, 3, 1, 0]
    assert (executeInstructionsn(n=2, startPos=[1, 1], s="LURD")) == [4, 1, 0, 0]
    assert (executeInstructionsn(n=1, startPos=[0, 0], s="LRUD")) == [0, 0, 0, 0]
    assert (executeInstructionsn(n=500, startPos=[499, 499], s="L")) == [1]
