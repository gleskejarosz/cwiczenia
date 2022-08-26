import string


def minTimeToType(word: str) -> int:
    alphabet = list(string.ascii_lowercase)
    number = [x for x in range(0, 27)]
    alphabet_dict = {k: v for (k, v) in zip(alphabet, number)}

    min_time = 0
    prev_pos = 0

    for letter in word:
        pos = alphabet_dict[letter]
        if pos > prev_pos:
            cw_time = abs(pos - prev_pos)
            cww_time = abs(prev_pos + 26 - pos)
        else:
            cw_time = abs(26 - prev_pos + pos)
            cww_time = abs(prev_pos - pos)
        min_time += min(cw_time, cww_time) + 1
        prev_pos = pos

    return min_time


if __name__ == '__main__':
    assert(minTimeToType("abc")) == 5
    assert(minTimeToType("bza")) == 7
    assert(minTimeToType("zjpc")) == 34
