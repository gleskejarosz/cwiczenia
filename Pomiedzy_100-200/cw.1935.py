def canBeTypedWords(text: str, brokenLetters: str) -> int:
    text_list = text.split(" ")
    count = 0
    temp_count = 0

    for word in text_list:
        for letter in word:
            if letter not in brokenLetters:
                temp_count += 1
        if temp_count == len(word):
            count += 1
        temp_count = 0

    return count


if __name__ == '__main__':
    assert (canBeTypedWords(text="hello world", brokenLetters="ad")) == 1
    assert (canBeTypedWords(text="leet code", brokenLetters="lt")) == 1
    assert (canBeTypedWords(text="leet code", brokenLetters="e")) == 0
