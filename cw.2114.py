def mostWordsFound(sentences):
    space = 0
    words = []
    for sentence in sentences:
        for letter in sentence:
            if letter == " ":
                space += 1
        words.append(space + 1)
        space = 0
    return max(words)


if __name__ == '__main__':
    assert(mostWordsFound(["alice and bob love leetcode", "i think so too",
                            "this is great thanks very much"])) == 6
    assert(mostWordsFound(["please wait", "continue to fight", "continue to win"])) == 3
