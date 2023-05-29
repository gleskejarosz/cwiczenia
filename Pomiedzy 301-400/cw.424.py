def characterReplacement(s: str, k: int) -> int:
    left = 0
    freq = {}
    maxlen = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        cur_len = right - left + 1
        if cur_len - max(freq.values()) <= k:
            maxlen = max(maxlen, cur_len)
        else:
            freq[s[left]] -= 1
            left += 1

    return maxlen


if __name__ == '__main__':
    assert (characterReplacement(s="ABAB", k=2)) == 4
    assert (characterReplacement(s="AABABBA", k=1)) == 4
