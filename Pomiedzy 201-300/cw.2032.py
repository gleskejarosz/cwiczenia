def twoOutOfThree(nums1: list, nums2: list, nums3: list) -> list:
    result = []
    nums = nums1 + nums2 + nums3
    nums = set(nums)
    test_num = 0

    for num in nums:
        if num in nums1:
            test_num += 1
        if num in nums2:
            test_num += 1
        if num in nums3:
            test_num += 1
        if test_num >= 2:
            result.append(num)
        test_num = 0

    return result


if __name__ == '__main__':
    assert (twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3])) == [2, 3]
    assert (twoOutOfThree(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2])) == [1, 2, 3]
    assert (twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5])) == []
