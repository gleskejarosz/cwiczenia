def diStringMatch(s: str) -> list:
    s_len = len(s) + 1
    result = [x for x in range(s_len)]

    if s[0] == "D":
        result = sorted(result, reverse=True)

    cycle = 1
    changed = 0
    cycles = 2

    while cycle < cycles:
        for idx, letter in enumerate(s):
            if letter == "I":
                if result[idx + 1] < result[idx]:
                    result[idx + 1], result[idx] = result[idx], result[idx + 1]
                    changed += 1
            else:
                if result[idx + 1] > result[idx]:
                    result[idx + 1], result[idx] = result[idx], result[idx + 1]
                    changed += 1
        if changed > 0:
            cycles += 1
        cycle += 1
        changed = 0

    return result


if __name__ == '__main__':
    assert (diStringMatch("DDI")) == [3, 2, 0, 1]
    assert (diStringMatch("IDID")) == [0, 2, 1, 4, 3]
    assert (diStringMatch("III")) == [0, 1, 2, 3]
    assert (diStringMatch("IDD")) == [0, 3, 2, 1]
