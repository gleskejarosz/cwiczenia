def maxPower(s: str) -> int:
    counter = []
    count_letter = 1
    s_len = len(s)

    for idx, letter in enumerate(s):
        if idx + 1 == s_len:
            break
        if letter == s[idx + 1]:
            count_letter += 1
        else:
            counter.append(count_letter)
            count_letter = 1
    counter.append(count_letter)

    return max(counter)


if __name__ == '__main__':
    assert(maxPower("leetcode")) == 2
    assert(maxPower("abbcccddddeeeeedcba")) == 5
    assert(maxPower("aaaaaaaaabbbbbbbbbbb")) == 11
