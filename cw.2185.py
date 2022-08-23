def prefixCount(words: list, pref: str) -> int:
    count = 0

    for word in words:
        if word.startswith(pref) is True:
            count += 1

    return count


if __name__ == '__main__':
    assert (prefixCount(words=["pay", "attention", "practice", "attend"], pref="at")) == 2
    assert (prefixCount(words=["leetcode", "win", "loops", "success"], pref="code")) == 0
