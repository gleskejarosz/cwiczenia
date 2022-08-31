def findWords(words: list) -> list:
    first_row = "qwertyuiop"
    second_row = "asdfghjkl"
    third_row = "zxcvbnm"
    rows_dict = {}
    for letter in first_row:
        rows_dict[letter] = 1
    for letter in second_row:
        rows_dict[letter] = 2
    for letter in third_row:
        rows_dict[letter] = 3

    prev_row = 0
    yes = 0
    result = []
    for word in words:
        for letter in word.lower():
            temp_row = rows_dict[letter]
            if temp_row != prev_row and prev_row > 0:
                yes = 0
                break
            prev_row = temp_row
            yes = 1
        prev_row = 0
        if yes == 1:
            result.append(word)
        yes = 0

    return result


if __name__ == '__main__':
    assert (findWords(["Hello", "Alaska", "Dad", "Peace"])) == ["Alaska", "Dad"]
    assert (findWords(["omk"])) == []
    assert (findWords(["adsdf", "sfd"])) == ["adsdf", "sfd"]
