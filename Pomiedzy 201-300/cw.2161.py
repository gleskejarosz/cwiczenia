def pivotArray(nums: list, pivot: int) -> list:
    left_side = []
    right_side = []
    center = []

    for num in nums:
        if num < pivot:
            left_side.append(num)
        if num > pivot:
            right_side.append(num)
        if num == pivot:
            center.append(num)

    result = left_side + center + right_side

    return result


if __name__ == '__main__':
    assert (pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10)) == [9, 5, 3, 10, 10, 12, 14]
    assert (pivotArray(nums=[-3, 4, 3, 2], pivot=2)) == [-3, 2, 4, 3]
