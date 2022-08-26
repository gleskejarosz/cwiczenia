def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    len1 = len(word1)
    len2 = len(word2)
    loops = max(len1, len2)

    for pos in range(loops):
        if pos < len(word1):
            result += word1[pos]
        else:
            result += ""
        if pos < len(word2):
            result += word2[pos]
        else:
            result += ""

    return result


if __name__ == '__main__':
    assert (mergeAlternately(word1="abc", word2="pqr")) == "apbqcr"
    assert (mergeAlternately(word1="ab", word2="pqrs")) == "apbqrs"
    assert (mergeAlternately(word1="abcd", word2="pq")) == "apbqcd"
