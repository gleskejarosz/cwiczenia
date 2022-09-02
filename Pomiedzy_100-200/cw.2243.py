def digitSum(s: str, k: int) -> str:
    groups = []
    digits = []
    sum_group = 0
    new_s = "a" * (k + 1)

    if len(s) <= k:
        return s

    while len(new_s) > k:
        list_s = list(s)
        for idx in range(0, len(s), k):
            elem = list_s[idx: idx + k]
            groups.append(elem)

        for group in groups:
            for num in group:
                sum_group += int(num)
            digits.append(sum_group)
            sum_group = 0

        new_s = ""
        for elem in digits:
            new_s += str(elem)

        if len(new_s) <= k:
            return new_s
        groups = []
        digits = []
        sum_group = 0
        s = new_s

    return new_s


if __name__ == '__main__':
    assert (digitSum(s="11111222223", k=3)) == "135"
    assert (digitSum(s="00000000", k=3)) == "000"
    assert (digitSum(s="233", k=3)) == "233"
