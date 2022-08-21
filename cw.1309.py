import string


def freqAlphabets(s: str) -> str:
    alphabet = list(string.ascii_lowercase)
    numbers = []
    result = ""

    for n in range(1, 27):
        numbers.append(str(n))

    transl_dict = {k: v for (k, v) in zip(numbers, alphabet)}

    list_s = s.split("#")
    updated_list = []
    if list_s[-1] == "":
        list_s = list_s[0:-1]

    for elem in list_s:
        updated_list.append(elem[-2:])
        if len(elem) > 2:
            for l in elem[0: -2]:
                updated_list.insert(-1, l)
    if not s.endswith("#"):
        for l in updated_list[-1]:
            updated_list.insert(-1, l)
        updated_list = updated_list[0: -1]

    for elem in updated_list:
        letter = transl_dict[elem]
        result += letter

    return result


if __name__ == '__main__':
    assert(freqAlphabets("10#11#12")) == "jkab"
    assert(freqAlphabets("1326#")) == "acz"
    assert(freqAlphabets("719#26#421#14#11#22#817#417#10#10#25#")) == "gszdunkvhqdqjjy"
