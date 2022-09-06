import string


def sortString(s: str) -> str:
    alphabet = list(string.ascii_lowercase)
    number = [x for x in range(26)]
    alphabet_dict2 = {k: v for k, v in zip(alphabet, number)}
    s_list = list(s)
    result = ""
    s_set = sorted({x for x in s})
    check_dict = {}
    nums = []

    for letter in s_set:
        num = alphabet_dict2[letter]
        nums.insert(0, num)
        check_dict[num] = letter

    while s_list:
        for num in check_dict:
            letter = check_dict[num]
            if letter in s_list:
                result += letter
                s_list.remove(letter)

        for num in nums:
            letter = check_dict[num]
            if letter in s_list:
                result += letter
                s_list.remove(letter)

    return result


if __name__ == '__main__':
    assert(sortString("aaaabbbbcccc")) == "abccbaabccba"
    assert(sortString("rat")) == "art"
