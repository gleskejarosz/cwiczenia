import string


def reverseOnlyLetters(s: str) -> str:
    alphabet = string.ascii_letters
    s_reversed = list(s[::-1])
    indexes = []

    for idx, elem in enumerate(s_reversed):
        if elem not in alphabet:
            indexes.append(idx)

    for index in indexes[::-1]:
        s_reversed.pop(index)

    for idx, elem in enumerate(s):
        if elem not in alphabet:
            s_reversed.insert(idx, elem)

    result = ""

    for elem in s_reversed:
        result += elem

    return result


if __name__ == '__main__':
    assert(reverseOnlyLetters("ab-cd")) == "dc-ba"
    assert(reverseOnlyLetters("a-bC-dEf-ghIj")) == "j-Ih-gfE-dCba"
    assert(reverseOnlyLetters("Test1ng-Leet=code-Q!")) == "Qedo1ct-eeLg=ntse-T!"
    assert(reverseOnlyLetters("7_28]")) == "7_28]"
