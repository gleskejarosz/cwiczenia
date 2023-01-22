def partition(s: str) -> list:
    result = []
    s_len = len(s)

    def extend(i, sub_list):
        if i >= s_len:
            result.append(sub_list)
        substring = ""
        for j in range(i, s_len):
            substring += s[j]
            if substring == substring[::-1]:
                extend(j + 1, sub_list + [substring])

    extend(0, [])
    return result


if __name__ == '__main__':
    assert (partition("aab")) == [["a", "a", "b"], ["aa", "b"]]
    assert (partition("a")) == [["a"]]
