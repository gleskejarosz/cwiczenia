def rearrangeArray(nums: list) -> list:
    negative_int_idx = []
    positive_int_idx = []
    result = []

    for idx, num in enumerate(nums):
        if num < 0:
            negative_int_idx.append(idx)
        if num > 0:
            positive_int_idx.append(idx)

    for pos, index in enumerate(positive_int_idx):
        result.append(nums[index])
        negative_idx = negative_int_idx[pos]
        result.append(nums[negative_idx])

    return result


if __name__ == '__main__':
    assert (rearrangeArray([3, 1, -2, -5, 2, -4])) == [3, -2, 1, -5, 2, -4]
    assert (rearrangeArray([-1, 1])) == [1, -1]
