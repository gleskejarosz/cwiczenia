def firstPalindrome(words: list) -> str:
    for word in words:
        if word == word[::-1]:
            return word

    return ""


if __name__ == '__main__':
    assert (firstPalindrome(["abc", "car", "ada", "racecar", "cool"])) == "ada"
    assert (firstPalindrome(["notapalindrome", "racecar"])) == "racecar"
    assert (firstPalindrome(["def", "ghi"])) == ""
