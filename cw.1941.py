def areOccurrencesEqual(s: str) -> bool:
    s_set = set()

    for letter in s:
        s_set.add(letter)

    count = dict.fromkeys(s_set, 0)

    for letter in s:
        count[letter] += 1

    sample_val = list(count.values())[0]

    for elem in count:
        if count[elem] != sample_val:
            return False

    return True


if __name__ == '__main__':
    assert(areOccurrencesEqual("abacbc")) is True
    assert(areOccurrencesEqual("aaabb")) is False
