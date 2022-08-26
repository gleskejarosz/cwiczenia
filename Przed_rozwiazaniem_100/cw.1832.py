import string


def checkIfPangram(sentence: str) -> bool:
    alphabet = string.ascii_lowercase

    for letter in alphabet:
        if letter not in sentence:
            return False
    return True


if __name__ == '__main__':
    assert(checkIfPangram("thequickbrownfoxjumpsoverthelazydog")) is True
    assert(checkIfPangram("leetcode")) is False
