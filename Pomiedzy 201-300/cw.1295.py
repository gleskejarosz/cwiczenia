def findNumbers(nums: list) -> int:
    result = 0

    for num in nums:
        num_len = len(str(num))
        if num_len % 2 == 0:
            result += 1

    return result


if __name__ == '__main__':
    assert (findNumbers([12, 345, 2, 6, 7896])) == 2
    assert (findNumbers([555, 901, 482, 1771])) == 1
