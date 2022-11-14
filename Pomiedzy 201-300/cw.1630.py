def checkArithmeticSubarrays(nums: list, l: list, r: list) -> list:
    array_len = len(r)
    result = []
    temp_result = []
    prev = 0

    for idx in range(array_len):
        sub_array = nums[l[idx]: r[idx] + 1]
        sub_array = sorted(sub_array)
        difference = sub_array[1] - sub_array[0]
        test_difference = difference
        for index, num in enumerate(sub_array):
            if index == 0:
                prev = num
            else:
                test_difference = num - prev
            if test_difference != difference:
                result.append(False)
                temp_result.append(False)
                break
            else:
                temp_result.append(True)
            prev = num
        if temp_result.count(False) == 0:
            result.append(True)
        temp_result = []

    return result


if __name__ == '__main__':
    assert (checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5])) == [True, False, True]
    assert (checkArithmeticSubarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], l=[0, 1, 6, 4, 8, 7],
                                     r=[4, 4, 9, 7, 9, 10])) == [False, True, False, False, True, True]
