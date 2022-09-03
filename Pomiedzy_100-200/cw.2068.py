from collections import Counter


def checkAlmostEquivalent(word1: str, word2: str) -> bool:
    counter1 = Counter(word1)
    counter2 = Counter(word2)
    value = 0

    for key, item in counter1.items():
        if key in counter2:
            value = counter2[key]
        difference = abs(value - item)
        if difference > 3:
            return False
        value = 0

    for key, item in counter2.items():
        if key not in counter1:
            value = counter1[key]
            difference = abs(value - item)
            if difference > 3:
                return False

    return True


if __name__ == '__main__':
    assert (checkAlmostEquivalent(word1="aaaa", word2="bccb")) is False
    assert (checkAlmostEquivalent(word1="abcdeef", word2="abaaacc")) is True
    assert (checkAlmostEquivalent(word1="cccddabba", word2="babababab")) is True
    assert (checkAlmostEquivalent(word1="efcbfebbggbedgii", word2="fhgeccggbfihfggf")) is True
