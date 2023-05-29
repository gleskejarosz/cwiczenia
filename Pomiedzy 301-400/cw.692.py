def topKFrequent(words: list, k: int) -> list:
    words_dict = {}

    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    sorted_words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

    result = []
    pre_result = []
    pre_list = []
    prev_value = 0

    for idx, word in enumerate(sorted_words_dict):
        value = word[1]
        if value == prev_value:
            pre_list.append(word[0])
        elif idx >= k and value != prev_value:
            break
        else:
            if idx == 0:
                pre_list.append(word[0])
            else:
                pre_result.append(pre_list)
                pre_list = [word[0]]
        prev_value = value
    pre_result.append(pre_list)

    counter = 0
    for elem_list in pre_result:
        sorted_elem_list = sorted(elem_list)
        for elem in sorted_elem_list:
            if counter == k:
                break
            result.append(elem)
            counter += 1

    return result


if __name__ == '__main__':
    assert (topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=3)) == ["i", "love", "coding"]
    assert (topKFrequent(words=["love", "i", "leetcode", "i", "love", "coding"], k=2)) == ["i", "love"]
    assert (topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2)) == ["i", "love"]
    assert (topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                         k=4)) == ["the", "is", "sunny", "day"]
