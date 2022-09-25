def makeFancyString(s: str) -> str:
    s_len = len(s)
    result = ""

    for idx, letter in enumerate(s):
        if idx + 2 < s_len:
            if letter != s[idx + 1]:
                result += letter
            if letter == s[idx + 1] != s[idx + 2]:
                result += letter
        else:
            result += letter

    return result


if __name__ == '__main__':
    assert(makeFancyString("leeetcode")) == "leetcode"
    assert(makeFancyString("aaabaaaa")) == "aabaa"
    assert(makeFancyString("aab")) == "aab"
