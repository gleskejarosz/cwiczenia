from urllib3.connectionpool import xrange


def countBinarySubstrings(s: str) -> int:
    substrings_len = [1]
    for i in xrange(1, len(s)):
        if s[i - 1] != s[i]:
            substrings_len.append(1)
        else:
            substrings_len[-1] += 1

    result = 0
    for i in xrange(1, len(substrings_len)):
        result += min(substrings_len[i - 1], substrings_len[i])
    return result


if __name__ == '__main__':
    assert (countBinarySubstrings("00110011")) == 6
    assert (countBinarySubstrings("10101")) == 4
