def sortArrayByParity(nums: list) -> list:
    odd_int = []
    even_int = []

    for num in nums:
        if num % 2 == 0:
            even_int.append(num)
        else:
            odd_int.append(num)

    return even_int + odd_int


if __name__ == '__main__':
    assert (sortArrayByParity([3, 1, 2, 4])) == [2, 4, 3, 1]
    assert (sortArrayByParity([0])) == [0]
