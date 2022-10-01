def removeDuplicates(s: str) -> str:
    len_s = len(s)
    loop = len_s
    idx = 0

    while loop > 0:
        if idx + 1 >= len_s:
            idx = 0
        if s[idx] == s[idx + 1]:
            s = s[0: idx] + s[idx + 2:]
            loop += 1
            len_s -= 2
            if idx != 0:
                idx -= 2
            else:
                idx = -1
        idx += 1
        loop -= 1
        if s == "" or len(s) == 1:
            return s

    return s


if __name__ == '__main__':
    assert(removeDuplicates("abbaca")) == "ca"
    assert(removeDuplicates("azxxzy")) == "ay"
    assert(removeDuplicates("aababaab")) == "ba"
    assert(removeDuplicates("ibfjcaffccadidiaidchakchchcahabhibdcejkdkfbaeeaecdjhajbkfebebfea")) == \
          "ibfjcdidiaidchakchchcahabhibdcejkdkfbecdjhajbkfebebfea"
    assert(removeDuplicates("aaaaaaaa")) == ""
    assert(removeDuplicates("aaaaaaaaa")) == "a"
