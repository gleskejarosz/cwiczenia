def firstUniqChar(s: str) -> int:
    for idx, letter in enumerate(s):
        n = s[0: idx] + s[idx + 1:]
        if letter not in n:
            return idx
    return -1


if __name__ == '__main__':
    assert(firstUniqChar("leetcode")) == 0
    assert(firstUniqChar("loveleetcode")) == 2
    assert(firstUniqChar("aabb")) == -1
