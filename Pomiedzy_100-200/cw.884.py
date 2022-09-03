def uncommonFromSentences(s1: str, s2: str) -> list:
    s1_list = s1.split(" ")
    s2_list = s2.split(" ")
    s_list = s1_list + s2_list
    s_dict = {k: s_list.count(k) for k in s_list}
    result = []

    for word in s_dict:
        if s_dict[word] == 1:
            result.append(word)

    return result


if __name__ == '__main__':
    assert (uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour")) == ["sweet", "sour"]
    assert (uncommonFromSentences(s1="apple apple", s2="banana")) == ["banana"]
