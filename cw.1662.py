def arrayStringsAreEqual(word1, word2) -> bool:
    string1 = ""
    string2 = ""

    for word in word1:
        for letter in word:
            string1 += letter

    for word in word2:
        for letter in word:
            string2 += letter

    if string1 == string2:
        return True
    else:
        return False


if __name__ == '__main__':
    assert (arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"])) is True
    assert (arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"])) is False
    assert (arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"])) is True
