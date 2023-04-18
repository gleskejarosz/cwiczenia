def isAlienSorted(words: list, order: str) -> bool:
    word_nums_list = []

    for word in words:
        word_num = []
        for letter in word:
            idx = order.index(letter)
            word_num.append(idx)
        word_nums_list.append(word_num)

    word_nums = sorted(word_nums_list)

    for idx, word_elem in enumerate(word_nums_list):
        if word_nums[idx] != word_elem:
            return False

    return True


if __name__ == '__main__':
    assert (isAlienSorted(words=["kuvp", "q"], order="ngxlkthsjuoqcpavbfdermiywz")) is True
    assert (isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")) is True
    assert (isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")) is False
    assert (isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz")) is False
