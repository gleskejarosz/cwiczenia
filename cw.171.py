import string


def titleToNumber(columnTitle):
    alphabet = string.ascii_uppercase
    nums = []
    for n in range(1, 27):
        nums.append(n)
    dict_ex = {k: v for (k, v) in zip(alphabet, nums)}

    if len(columnTitle) == 1:
        return dict_ex[columnTitle]
    if len(columnTitle) == 2:
        return dict_ex[columnTitle[0]] * 26 + dict_ex[columnTitle[1]]
    if len(columnTitle) == 3:
        return dict_ex[columnTitle[0]] * 676 + dict_ex[columnTitle[1]] * 26 + dict_ex[columnTitle[2]]
    if len(columnTitle) == 4:
        return dict_ex[columnTitle[0]] * 17576 + dict_ex[columnTitle[1]] * 676 \
               + dict_ex[columnTitle[2]] * 26 + dict_ex[columnTitle[3]]
    if len(columnTitle) == 5:
        return dict_ex[columnTitle[0]] * 456976 + dict_ex[columnTitle[1]] * 17576 \
               + dict_ex[columnTitle[2]] * 676 + dict_ex[columnTitle[3]] * 26 \
               + dict_ex[columnTitle[4]]
    if len(columnTitle) == 6:
        return dict_ex[columnTitle[0]] * 11881376 + dict_ex[columnTitle[1]] * 456976 \
               + dict_ex[columnTitle[2]] * 17576 + dict_ex[columnTitle[3]] * 676 \
               + dict_ex[columnTitle[4]] * 26 + dict_ex[columnTitle[5]]
    if len(columnTitle) == 7:
        return dict_ex[columnTitle[0]] * 308915776 + dict_ex[columnTitle[1]] * 11881376 \
               + dict_ex[columnTitle[2]] * 456976 + dict_ex[columnTitle[3]] * 17576 \
               + dict_ex[columnTitle[4]] * 676 + dict_ex[columnTitle[5]] * 26 + dict_ex[columnTitle[6]]


if __name__ == '__main__':
    assert(titleToNumber("A")) == 1
    assert (titleToNumber("AB")) == 28
    assert (titleToNumber("ZY")) == 701
    print(titleToNumber("ZZZY"))
    print(titleToNumber("ZZZZX"))
