def percentageLetter(s: str, letter: str) -> int:
    s_len = len(s)
    letter_count = s.count(letter)

    result = int((letter_count / s_len) * 100)

    return result


if __name__ == '__main__':
    assert(percentageLetter(s = "foobar", letter = "o")) == 33
    assert(percentageLetter(s = "jjjj", letter = "k")) == 0
