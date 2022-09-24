def maxScore(s: str) -> int:
    counter = []

    for idx, elem in enumerate(s):
        if idx != 0:
            left = s[0: idx]
            right = s[idx:]
            score = left.count("0") + right.count("1")
            counter.append(score)

    return max(counter)


if __name__ == '__main__':
    assert(maxScore("011101")) == 5
    assert(maxScore("00111")) == 5
    assert(maxScore("1111")) == 3
