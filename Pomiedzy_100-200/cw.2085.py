def countWords(words1: list, words2: list) -> int:
    words1_dict = {k: words1.count(k) for k in words1}
    words2_dict = {k: words2.count(k) for k in words2}
    counter = 0

    for elem in words1_dict:
        if words1_dict[elem] == 1 and elem in words2_dict:
            if words2_dict[elem] == 1:
                counter += 1

    return counter


if __name__ == '__main__':
    assert (countWords(words1=["leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"])) == 2
    assert (countWords(words1=["b", "bb", "bbb"], words2=["a", "aa", "aaa"])) == 0
    assert (countWords(words1=["a", "ab"], words2=["a", "a", "a", "ab"])) == 1
