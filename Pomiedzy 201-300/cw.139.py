def wordBreak(s: str, wordDict: list) -> bool:
    word_set = set(wordDict)
    s_len = len(s)

    test_list = [False] * (s_len + 1)
    test_list[s_len] = True

    i = s_len

    while i >= 0:
        for j in range(i + 1, s_len + 1):
            a = test_list[j]
            b = s[i:j]
            if a is True and b in word_set:
                test_list[i] = True
                break
        i -= 1
    return test_list[0]


if __name__ == '__main__':
    assert (wordBreak(s="leetcode", wordDict=["leet", "code"])) is True
    assert (wordBreak(s="applepenapple", wordDict=["apple", "pen"])) is True
    assert (wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])) is False
