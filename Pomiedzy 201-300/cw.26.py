def removeDuplicates(nums):
    idx = 0
    while idx < len(nums):
        num = nums[idx]
        if num in nums[:idx]:
            nums.pop(idx)
            idx -= 1
        idx += 1
    return nums


if __name__ == '__main__':
    assert (removeDuplicates([1, 1, 2])) == [1, 2]
    assert (removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])) == [0, 1, 2, 3, 4]
