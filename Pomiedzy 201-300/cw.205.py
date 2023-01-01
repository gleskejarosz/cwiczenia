def isIsomorphic(s: str, t: str) -> bool:
    replacement = {}
    new_letters = []

    for idx, letter in enumerate(s):
        new_letter = t[idx]
        if letter in replacement and replacement[letter] != new_letter:
            return False
        if new_letter in new_letters and letter not in replacement:
            return False
        new_letters.append(new_letter)
        replacement[letter] = new_letter
    return True


if __name__ == '__main__':
    assert(isIsomorphic(s="badc", t="baba")) is False
    assert (isIsomorphic(s="egg", t="add")) is True
    assert (isIsomorphic(s="foo", t="bar")) is False
    assert (isIsomorphic(s="paper", t="title")) is True
