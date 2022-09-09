def stringMatching(words: list) -> list:
    result = set()

    for word in words:
        for elem in words:
            if elem in word and elem != word:
                result.add(elem)

    return list(result)


if __name__ == '__main__':
    assert (stringMatching(["mass", "as", "hero", "superhero"])) == ["as", "hero"]
    assert (stringMatching(["leetcode", "et", "code"])) == ["et", "code"]
    assert (stringMatching(["blue", "green", "bu"])) == []
