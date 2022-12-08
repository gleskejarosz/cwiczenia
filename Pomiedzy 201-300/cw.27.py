def removeElement(nums: list, val: int) -> int:
    counter = 0
    idx = 0
    nums_len = len(nums)

    for n in range(nums_len):
        num = nums[idx]
        if num == val:
            nums.pop(idx)
            nums.append("_")
            counter += 1
        else:
            idx += 1

    return len(nums) - counter


if __name__ == '__main__':
    assert(removeElement(nums=[3, 2, 2, 3], val=3)) == 2
    assert(removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)) == 5
