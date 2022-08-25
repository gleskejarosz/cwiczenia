import string


def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    alphabet = list(string.ascii_lowercase)[:10]
    number = list(x for x in range(0, 10))
    alphabet_dict = {k: v for (k, v) in zip(alphabet, number)}
    num1 = ""
    num2 = ""
    num3 = ""
    for letter in firstWord:
        num1 += str(alphabet_dict[letter])

    for letter in secondWord:
        num2 += str(alphabet_dict[letter])

    for letter in targetWord:
        num3 += str(alphabet_dict[letter])

    return int(num1) + int(num2) == int(num3)


if __name__ == '__main__':
    assert (isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb")) is True
    assert (isSumEqual(firstWord="aaa", secondWord="a", targetWord="aab")) is False
    assert (isSumEqual(firstWord="j", secondWord="j", targetWord="bi")) is True
    assert (isSumEqual(firstWord="aaa", secondWord="a", targetWord="aaaa")) is True