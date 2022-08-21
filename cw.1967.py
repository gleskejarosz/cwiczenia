def numOfStrings(patterns: list, word: str) -> int:
    count = 0

    for pattern in patterns:
        if pattern in word:
            count += 1

    return count


if __name__ == '__main__':
    assert (numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc")) == 3
    assert (numOfStrings(patterns=["a", "b", "c"], word="aaaaabbbbb")) == 2
    assert (numOfStrings(patterns=["a", "a", "a"], word="ab")) == 3
