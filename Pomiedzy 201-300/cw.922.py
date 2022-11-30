def sortArrayByParityII(nums: list) -> list:
    odd = []
    even = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    result = []

    for idx, num in enumerate(even):
        result.append(num)
        result.append(odd[idx])

    return result


if __name__ == '__main__':
    assert (sortArrayByParityII([4, 2, 5, 7])) == [4, 5, 2, 7]
    assert (sortArrayByParityII([2, 3])) == [2, 3]
