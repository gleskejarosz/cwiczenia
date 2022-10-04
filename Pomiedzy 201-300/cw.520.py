import string


def detectCapitalUse(word: str) -> bool:
    upper_cases = list(string.ascii_uppercase)
    word_len = len(word)
    counter = 0

    for letter in word:
        if letter in upper_cases:
            counter += 1

    if counter == word_len:
        return True

    for letter in word[1:]:
        if letter in upper_cases:
            return False

    return True


if __name__ == '__main__':
    assert(detectCapitalUse("USA")) is True
    assert (detectCapitalUse("leetcode")) is True
    assert(detectCapitalUse("FlaG")) is False
