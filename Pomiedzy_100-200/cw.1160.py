def countCharacters(words: list, chars: str) -> int:
    list_chars = list(chars)
    result = 0
    good = 1

    for word in words:
        for letter in word:
            if word.count(letter) > chars.count(letter):
                good = 0
                break
            if letter not in list_chars:
                good = 0
                break
        if good == 1:
            result += len(word)
        good = 1

    return result


if __name__ == '__main__':
    assert (countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach")) == 6
    assert (countCharacters(["hello", "world", "leetcode"], chars="welldonehoneyr")) == 10
