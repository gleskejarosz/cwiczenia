def sortedSquares(nums: list) -> list:
    result = []

    for num in nums:
        result.append(num ** 2)
    result.sort()

    return result


if __name__ == '__main__':
    assert (sortedSquares([-4, -1, 0, 3, 10])) == [0, 1, 9, 16, 100]
    assert (sortedSquares([-7, -3, 2, 3, 11])) == [4, 9, 9, 49, 121]
