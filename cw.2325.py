import string


def decodeMessage(key: str, message: str) -> str:
    alphabet = list(string.ascii_lowercase)
    new_key = []
    result = ""

    for letter in key:
        if letter not in new_key and letter != " ":
            new_key.append(letter)
        if letter == " ":
            pass

    code = {k: v for (k, v) in zip(new_key, alphabet)}

    for letter in message:
        if letter == " ":
            result += " "
        else:
            decoded_letter = code[letter]
            result += decoded_letter

    return result


if __name__ == '__main__':
    assert (decodeMessage(key="the quick brown fox jumps over the lazy dog",
                          message="vkbs bs t suepuv")) == "this is a secret"
    assert (decodeMessage(key="eljuxhpwnyrdgtqkviszcfmabo",
                          message="zwx hnfx lqantp mnoeius ycgk vcnjrdb")) == "the five boxing wizards jump quickly"
