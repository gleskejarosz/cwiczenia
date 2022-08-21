import string


def replaceDigits(s: str) -> str:
    alphabet = list(string.ascii_lowercase)
    numbers = []
    for n in range(1, 27):
        numbers.append(n)
    check_dict = {k: v for (k, v) in zip(alphabet, numbers)}
    replace_dict = {k: v for (k, v) in zip(numbers, alphabet)}
    result = ""
    list_s = list(s)
    prev_elem = list_s[0]

    for elem in list_s:
        if elem not in alphabet:
            pos_alp = check_dict[prev_elem]
            letter = replace_dict[pos_alp + int(elem)]
        else:
            letter = elem
            prev_elem = elem
        result += letter

    return result


if __name__ == '__main__':
    assert(replaceDigits("a1c1e1")) == "abcdef"
    assert(replaceDigits("a1b2c3d4e")) == "abbdcfdhe"
