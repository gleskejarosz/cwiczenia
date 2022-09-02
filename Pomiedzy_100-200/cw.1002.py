def commonChars(words: list) -> list:
    result = []
    check_dict = {}
    first_word = words[0]

    for letter in first_word:
        check_dict[letter] = first_word.count(letter)

    for letter in check_dict:
        for word in words[1:]:
            if letter in word:
                temp_count = word.count(letter)
                if temp_count < check_dict[letter]:
                    check_dict[letter] = temp_count
            else:
                check_dict[letter] = 0

    for elem in check_dict:
        qty = check_dict[elem]
        for q in range(qty):
            result.append(elem)

    return result


if __name__ == '__main__':
    assert (commonChars(["bella", "label", "roller"])) == ["e", "l", "l"]
    assert (commonChars(["cool", "lock", "cook"])) == ["c", "o"]
    