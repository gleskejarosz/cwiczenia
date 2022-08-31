import string


def minDeletionSize(strs: list) -> int:
    alphabet = list(string.ascii_lowercase)
    number = [x for x in range(26)]
    alp_dict = {k: v for k, v in zip(alphabet, number)}
    columns = [[] for x in range(len(strs[0]))]
    counter = 0
    idx = 0

    for elem in strs:
        for letter in elem:
            pos = alp_dict[letter]
            columns[idx].append(pos)
            idx += 1
        idx = 0

    for c in columns:
        if len(c) == 1:
            return 0
        for idx in range(1, len(c)):
            if c[idx] < c[idx - 1]:
                counter += 1
                break

    return counter


if __name__ == '__main__':
    assert (minDeletionSize(["cba", "daf", "ghi"])) == 1
    assert (minDeletionSize(["a", "b"])) == 0
    assert (minDeletionSize(["zyx", "wvu", "tsr"])) == 3
    assert (minDeletionSize(["rrjk", "furt", "guzm"])) == 2
