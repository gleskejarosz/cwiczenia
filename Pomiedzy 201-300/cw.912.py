def sortArray(nums: list) -> list:

    for i in range(len(nums) // 2, -1, -1):
        max_heapify(nums, i, len(nums))

    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        max_heapify(nums, 0, i)

    return nums


def max_heapify(nums, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(nums, largest, n)


if __name__ == '__main__':
    assert (sortArray([5, 2, 3, 1])) == [1, 2, 3, 5]
    assert (sortArray([5, 1, 1, 2, 0, 0])) == [0, 0, 1, 1, 2, 5]
    