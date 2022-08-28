def maxProduct(nums: list) -> int:
    max_elem = [0, 0]
    for elem in nums:
        if elem > max_elem[0]:
            temp = max_elem[0]
            max_elem[0] = elem
            max_elem[1] = temp
        elif elem > max_elem[1]:
            max_elem[1] = elem
    return (max_elem[0] - 1) * (max_elem[1] - 1)


if __name__ == '__main__':
    assert (maxProduct([3, 4, 5, 2])) == 12
    assert (maxProduct([1, 5, 4, 5])) == 16
    assert (maxProduct([3, 7])) == 12
