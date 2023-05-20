from functools import reduce


def pivotIndex(nums: list) -> int:
    idx_r = 1
    l_sum = 0

    r_sum = reduce((lambda x, y: x + y), nums)
    while idx_r < len(nums):
        middle = nums[idx_r - 1]
        r_sum -= middle
        if l_sum == r_sum:
            return idx_r - 1
        l_sum += middle
        idx_r += 1

    if l_sum == 0:
        return idx_r - 1
    return -1


if __name__ == '__main__':
    assert (pivotIndex([-1, -1, 0, 1, 1, 0])) == 5
    assert (pivotIndex([1, 7, 3, 6, 5, 6])) == 3
    assert (pivotIndex([1, 2, 3])) == -1
    assert (pivotIndex([2, 1, -1])) == 0
