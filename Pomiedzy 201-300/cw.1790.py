def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    indexes = []
    counter = 0

    for idx, letter in enumerate(s1):
        if letter != s2[idx]:
            indexes.append(idx)
            counter += 1
        if counter > 2:
            return False

    if len(indexes) == 1:
        return False

    letter_1 = s1[indexes[0]]
    letter_2 = s1[indexes[1]]

    swapped_word = s1[0:indexes[0]] + letter_2 + s1[indexes[0] + 1:indexes[1]] + letter_1 + s1[indexes[1] + 1:]
    if swapped_word == s2:
        return True

    return False


if __name__ == '__main__':
    assert (areAlmostEqual(s1="aa", s2="ac")) is False
    assert (areAlmostEqual(s1="bank", s2="kanb")) is True
    assert (areAlmostEqual(s1="attack", s2="defend")) is False
    assert (areAlmostEqual(s1="kelb", s2="kelb")) is True
