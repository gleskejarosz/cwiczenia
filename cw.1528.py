def restoreString(s, indices):
    s_dict = {k: v for (k, v) in zip(indices, s)}
    result = ""
    for n in range(0, len(s)):
        result += s_dict[n]
    return result


if __name__ == '__main__':
    assert(restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3])) == "leetcode"
    assert(restoreString(s="abc", indices=[0, 1, 2])) == "abc"
