import string


def numberOfLines(widths: list, s: str) -> list:
    list_s = list(s)
    alphabet = string.ascii_lowercase
    s_dict = {k: v for k, v in zip(alphabet, widths)}
    sum_line = 0
    lines = 0
    last_sum = 0

    for elem in list_s:
        value = s_dict[elem]
        sum_line += value
        if sum_line > 100:
            sum_line = value
            lines += 1
        if sum_line == 100:
            last_sum = sum_line
            sum_line = 0
            lines += 1

    if sum_line > 0:
        lines += 1
        return [lines, sum_line]

    if sum_line == 0:
        return [lines, last_sum]


if __name__ == '__main__':
    assert (numberOfLines(
        widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        s="abcdefghijklmnopqrstuvwxyz")) == [3, 60]
    assert (numberOfLines(
        widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        s="bbbcccdddaaa")) == [2, 4]
    assert (numberOfLines(widths=[3, 4, 10, 4, 8, 7, 3, 3, 4, 9, 8, 2, 9, 6, 2, 8, 4, 9, 9, 10, 2, 4, 9, 10, 8, 2], s=
    "mqblbtpvicqhbrejb")) == [1, 100]
