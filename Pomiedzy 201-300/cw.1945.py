import string


def getLucky(s: str, k: int) -> int:
    alphabet = list(string.ascii_lowercase)
    nums = [x for x in range(27) if x > 0]
    alp_dict = {k: v for k, v in zip(alphabet, nums)}
    s_nums = ""
    counter = 1
    s_nums_sum = 0

    for letter in s:
        s_nums += str(alp_dict[letter])

    while counter <= k:
        for num in s_nums:
            s_nums_sum += int(num)
        if counter == k:
            break
        s_nums = ""
        nums_sum_str = str(s_nums_sum)
        for s_sum in nums_sum_str:
            s_nums += s_sum
        counter += 1
        s_nums_sum = 0

    return s_nums_sum


if __name__ == '__main__':
    assert (getLucky(s="iiii", k=1)) == 36
    assert (getLucky(s="leetcode", k=2)) == 6
    assert (getLucky(s="zbax", k=2)) == 8
