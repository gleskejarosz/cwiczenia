def isAnagram(s: str, t: str) -> bool:
    t_list = sorted(list(t))
    s_list = sorted(list(s))

    if t_list == s_list:
        return True
    return False


def isAnagram2(s: str, t: str) -> bool:
    t_dict = {k: t.count(k) for k in t}
    s_dict = {k: s.count(k) for k in s}

    if t_dict == s_dict:
        return True
    return False


if __name__ == '__main__':
    assert (isAnagram(s="anagram", t="nagaram")) is True
    assert (isAnagram(s="rat", t="car")) is False
    assert (isAnagram2(s="anagram", t="nagaram")) is True
    assert (isAnagram2(s="rat", t="car")) is False
