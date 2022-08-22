import string


def repeatedCharacter(s: str) -> str:
    alphabet = string.ascii_lowercase
    count = dict.fromkeys(alphabet, 0)

    for letter in s:
        count[letter] += 1
        if count[letter] == 2:
            return letter


if __name__ == '__main__':
    assert(repeatedCharacter("abccbaacz")) == "c"
    assert(repeatedCharacter("abcdd")) == "d"
