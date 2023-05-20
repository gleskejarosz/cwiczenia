def isSubsequence(s: str, t: str) -> bool:
    indexes = []
    letter_idx = []

    for s_letter in s:
        s_counter = s.count(s_letter)
        t_counter = t.count(s_letter)
        if s_counter > t_counter:
            return False
        if s_letter in t:
            for idx, letter in enumerate(t):
                if letter == s_letter:
                    letter_idx.append(idx)
            indexes.append(letter_idx)
            letter_idx = []
        else:
            return False
    prev_idx = -1
    curr_idx = -1
    for idx_list in indexes:
        for idx in idx_list:
            if idx > prev_idx:
                curr_idx = idx
                break
        if prev_idx == curr_idx:
            return False
        prev_idx = curr_idx

    return True


if __name__ == '__main__':
    assert(isSubsequence(s="ab", t="baab")) is True
    assert (isSubsequence(s="aaaaaa", t="bbaaaa")) is False
    assert (isSubsequence(s="abc", t="ahbgdc")) is True
    assert (isSubsequence(s="axc", t="ahbgdc")) is False
