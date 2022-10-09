def singleNumber(nums):
    nums_dict = {k: nums.count(k) for k in nums}

    for num in nums_dict:
        if nums_dict[num] == 1:
            return num


if __name__ == '__main__':
    assert(singleNumber([10, 9, 1, 2, 3, 5, 6, 7, 8, 9, 1, 2, 3, 5, 6, 7, 8])) == 10
    assert(singleNumber([1, 2, 3, 5, 6, 7, 8, 9, 1, 2, 3, 5, 6, 7, 8])) == 9
    assert(singleNumber([2, 2, 1])) == 1
    assert(singleNumber([4, 1, 2, 1, 2])) == 4
    assert(singleNumber([1])) == 1
    assert(singleNumber([1, 2, 2])) == 1
