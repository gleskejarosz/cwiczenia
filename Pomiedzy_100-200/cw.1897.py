import string


def makeEqual(words: list) -> bool:
    words_len = len(words)
    alphabet = string.ascii_lowercase
    words_dict = {k: 0 for k in alphabet}

    for word in words:
        for letter in word:
            words_dict[letter] += 1

    new_words_dict = {k: words_dict[k] for k in words_dict if words_dict[k] > 0}

    for elem in new_words_dict:
        if new_words_dict[elem] % words_len != 0:
            return False

    return True


if __name__ == '__main__':
    assert (makeEqual(["abc", "aabc", "bc"])) is True
    assert (makeEqual(["ab", "a"])) is False
    assert (makeEqual(["a", "b"])) is False
    assert (makeEqual(["b"])) is True
    assert (makeEqual(["a", "a", "a"])) is True
    