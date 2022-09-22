def findTheDifference(s: str, t: str) -> str:
    s_dict = {k: s.count(k) for k in t}
    t_dict = {k: t.count(k) for k in t}

    for elem in s_dict:
        qty = s_dict[elem]
        if qty != t_dict[elem]:
            return elem


if __name__ == '__main__':
    assert (findTheDifference(s="abcd", t="abcde")) == "e"
    assert (findTheDifference(s="", t="y")) == "y"
