def backspaceCompare(s: str, t: str) -> bool:
    final_s = ""
    final_t = ""

    for letter in s:
        if letter == "#":
            final_s_len = len(final_s)
            if final_s_len >= 1:
                final_s = final_s[:-1]
        else:
            final_s += letter

    for letter in t:
        if letter == "#":
            final_t_len = len(final_t)
            if final_t_len >= 1:
                final_t = final_t[:-1]
        else:
            final_t += letter

    if final_t == final_s:
        return True
    else:
        return False


if __name__ == '__main__':
    assert (backspaceCompare(s="ab#c", t="ad#c")) is True
    assert (backspaceCompare(s="ab##", t="c#d#")) is True
    assert (backspaceCompare(s="a#c", t="b")) is False
