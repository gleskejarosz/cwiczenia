def longestPalindrome(s: str) -> int:
    counter = 0
    s_len = len(s)
    word = set(s)

    for letter in word:
        qty = s.count(letter)
        if qty % 2 == 1:
            counter += 1

    if counter == 0:
        return s_len
    else:
        return s_len - counter + 1


if __name__ == '__main__':
    assert (longestPalindrome("bb")) == 2
    assert(longestPalindrome("abccccdd")) == 7
    assert(longestPalindrome("a")) == 1
