def numIdenticalPairs(nums: list) -> int:
    nums_dict = {k: nums.count(k) for k in nums}
    count = 0
    single_count = 0

    for elem in nums_dict:
        elem_v = nums_dict[elem]
        if elem_v > 1:
            num = elem_v - 1
            for n in range(1, num + 1):
                single_count += n
            count += single_count
            single_count = 0

    return count


if __name__ == '__main__':
    assert (numIdenticalPairs([1, 2, 3, 1, 1, 3])) == 4
    assert (numIdenticalPairs([1, 1, 1, 1])) == 6
    assert (numIdenticalPairs([1, 2, 3])) == 0
