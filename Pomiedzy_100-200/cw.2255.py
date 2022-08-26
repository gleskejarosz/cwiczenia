def countPrefixes(words: list, s: str) -> int:
    count = 0
    s_len = len(s)

    for word in words:
        word_len = len(word)
        pos = min(s_len, word_len)
        if word == s[0: pos]:
            count += 1

    return count


if __name__ == '__main__':
    assert (countPrefixes(words=["a", "b", "c", "ab", "bc", "abc"], s="abc")) == 3
    assert (countPrefixes(words=["a", "a"], s="aa")) == 2
    assert (countPrefixes(words=["feh","w","w","lwd","c","s","vk","zwlv","n","w","sw","qrd","w","w","mqe","w","w","w",
                                 "gb","w","qy","xs","br","w","rypg","wh","g","w","w","fh","w","w","sccy"], s="w")) == 14
