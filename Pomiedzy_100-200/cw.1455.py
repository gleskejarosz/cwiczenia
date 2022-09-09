def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    sentence_list = sentence.split(" ")
    search_word_len = len(searchWord)

    for idx, word in enumerate(sentence_list):
        if searchWord == word[:search_word_len]:
            return idx + 1

    return -1


if __name__ == '__main__':
    assert (isPrefixOfWord(sentence="i love eating burger", searchWord="burg")) == 4
    assert (isPrefixOfWord(sentence="this problem is an easy problem", searchWord="pro")) == 2
    assert (isPrefixOfWord(sentence="i am tired", searchWord="you")) == -1
    assert(isPrefixOfWord(sentence="hellohello hellohellohello", searchWord="ell")) == -1
