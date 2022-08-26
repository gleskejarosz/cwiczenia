def checkString(s: str) -> bool:
    s_list = list(s)

    a_idx = [i for i, s in enumerate(s_list) if 'a' in s]
    b_idx = [i for i, s in enumerate(s_list) if 'b' in s]

    for elem_a in a_idx:
        for elem_b in b_idx:
            if elem_a > elem_b:
                return False

    return True


if __name__ == '__main__':
    assert(checkString("aaabbb")) is True
    assert(checkString("abab")) is False
    assert(checkString("bbb")) is True
