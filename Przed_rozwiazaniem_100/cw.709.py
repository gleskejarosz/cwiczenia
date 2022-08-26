import string


def toLowerCase(s: str) -> str:
    # alphabet_l = string.ascii_uppercase
    # alphabet_s = string.ascii_lowercase
    # alphabet = {k: v for (k, v) in zip(alphabet_l, alphabet_s)}
    # result = ""
    #
    # for letter in s:
    #     if letter in alphabet_l:
    #         result += alphabet[letter]
    #     else:
    #         result += letter
    #
    # return result

    result = s.lower()
    return result


if __name__ == '__main__':
    assert(toLowerCase("Hello")) == "hello"
    assert(toLowerCase("here")) == "here"
    assert(toLowerCase("LOVELY")) == "lovely"
