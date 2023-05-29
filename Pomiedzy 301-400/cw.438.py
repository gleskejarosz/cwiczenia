import string


def findAnagrams(s: str, p: str) -> list:
    result, len_p, len_s = [], len(p), len(s)
    alphabet = list(string.ascii_lowercase)
    nums = [0 for x in range(26)]
    p_dict = dict(zip(alphabet, nums))

    if len_p > len_s:
        return []

    for char in p:
        p_dict[char] += 1

    for idx in range(len_p - 1):
        if s[idx] in p_dict:
            p_dict[s[idx]] -= 1

    for idx in range(-1, len_s - len_p + 1):
        if idx > -1 and s[idx] in p_dict:
            p_dict[s[idx]] += 1
        if idx + len_p < len_s and s[idx + len_p] in p_dict:
            p_dict[s[idx + len_p]] -= 1

        if all(value == 0 for value in p_dict.values()):
            result.append(idx + 1)

    return result


if __name__ == '__main__':
    assert (findAnagrams(s="baa", p="aa")) == [1]
    assert (findAnagrams(s="cbaebabacd", p="abc")) == [0, 6]
    assert (findAnagrams(s="abab", p="ab")) == [0, 1, 2]
