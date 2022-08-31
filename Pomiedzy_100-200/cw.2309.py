import string


def greatestLetter(s: str) -> str:
    alphabet_a = string.ascii_lowercase
    alphabet_b = string.ascii_uppercase
    number = [x for x in range(26)]
    alphabet_a_dict = {k: v for k, v in zip(alphabet_a, number)}
    alphabet_b_dict = {k: v for k, v in zip(alphabet_b, number)}
    letter_dict = {k: v for k, v in zip(number, alphabet_b_dict)}
    s_list = list(s)
    list_a = []
    list_b = []
    result = []

    for letter in s_list:
        if letter in alphabet_a:
            list_a.append(alphabet_a_dict[letter])
        else:
            list_b.append(alphabet_b_dict[letter])

    for num in list_a:
        if num in list_b:
            result.append(num)

    if len(result) == 0:
        return ""

    return letter_dict[max(result)]


if __name__ == '__main__':
    assert(greatestLetter("lEeTcOdE")) == "E"
    assert(greatestLetter("arRAzFif")) == "R"
    assert(greatestLetter("AbCdEfGhIjK")) == ""
