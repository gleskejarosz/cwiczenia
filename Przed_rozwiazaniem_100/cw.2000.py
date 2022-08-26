def reversePrefix(word: str, ch: str) -> str:
    word_list = list(word)

    if ch in word:
        pos = word_list.index(ch)
    else:
        return word

    prefix = word_list[0: pos + 1][::-1]
    word_end = word_list[pos + 1:]

    result = ""
    for letter in (prefix + word_end):
        result += letter

    return result


if __name__ == '__main__':
    assert (reversePrefix(word="abcdefd", ch="d")) == "dcbaefd"
    assert (reversePrefix(word="xyxzxe", ch="z")) == "zxyxxe"
    assert (reversePrefix(word="abcd", ch="z")) == "abcd"
