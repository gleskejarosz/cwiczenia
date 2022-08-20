def countConsistentStrings(allowed, words) -> int:
    allowed_letters = list(allowed)
    temp_sum = 0
    count = 0

    for word in words:
        for letter in word:
            if letter in allowed_letters:
                temp_sum += 1
            if temp_sum == len(word):
                count += 1
        temp_sum = 0

    return count


if __name__ == '__main__':
    assert (countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"])) == 2
    assert (countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"])) == 7
    assert (countConsistentStrings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"])) == 4
