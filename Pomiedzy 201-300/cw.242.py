def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for letter in s:
        if letter not in t:
            return False
        else:
            if s.count(letter) != t.count(letter):
                return False

    return True


if __name__ == '__main__':
    assert(isAnagram(s="a", t="ab")) is False
    assert (isAnagram(s="anagram", t="nagaram")) is True
    assert (isAnagram(s="rat", t="car")) is False
