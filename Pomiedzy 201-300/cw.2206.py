def divideArray(nums: list) -> bool:
    nums_dict = {k: nums.count(k) for k in nums}

    for num in nums_dict:
        if nums_dict[num] % 2 != 0:
            return False
    return True


if __name__ == '__main__':
    assert (divideArray([3, 2, 3, 2, 2, 2])) is True
    assert (divideArray([1, 2, 3, 4])) is False
