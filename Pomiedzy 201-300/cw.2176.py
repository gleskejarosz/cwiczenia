def countPairs(nums: list, k: int) -> int:
    results = []
    counter = 0
    nums_len = len(nums)

    for idx, num in enumerate(nums):
        if idx + 1 == nums_len:
            break
        for pos, n in enumerate(nums[idx + 1:]):
            if num == n:
                results.append(idx * (pos + idx + 1))

    for elem in results:
        if elem % k == 0:
            counter += 1

    return counter


if __name__ == '__main__':
    assert (countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2)) == 4
    assert (countPairs(nums=[1, 2, 3, 4], k=1)) == 0
