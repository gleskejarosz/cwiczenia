def divisorSubstrings(num: int, k: int) -> int:
    counter = 0
    nums = []
    num_str = str(num)
    num_len = len(num_str)

    for idx, elem in enumerate(num_str):
        if idx + k > num_len:
            break
        number = num_str[idx: idx + k]
        nums.append(int(number))

    nums_filtered = list(filter(lambda x: (x > 0), nums))

    for n in nums_filtered:
        if num % n == 0:
            counter += 1

    return counter


if __name__ == '__main__':
    assert (divisorSubstrings(num=240, k=2)) == 2
    assert (divisorSubstrings(num=430043, k=2)) == 2
    assert(divisorSubstrings(num=2, k=1)) == 1
    assert(divisorSubstrings(num=60000, k=3)) == 1
