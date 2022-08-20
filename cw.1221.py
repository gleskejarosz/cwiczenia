def balancedStringSplit(s):
    count = 0
    temp_count = 0
    loops = 0

    for elem in s:
        if elem == "R":
            temp_count += 0
            loops += 1
        else:
            temp_count += 1
            loops += 1
        s = s[1: len(s)]
        if loops % 2 == 0 and temp_count == loops / 2:
            count += 1
            temp_count = 0
            loops = 0
    return count


if __name__ == '__main__':
    assert(balancedStringSplit("RLRRLLRLRL")) == 4
    assert(balancedStringSplit("RLRRRLLRLL")) == 2
    assert (balancedStringSplit("RLRRRRRRRRLLLLLLLRLL")) == 2
