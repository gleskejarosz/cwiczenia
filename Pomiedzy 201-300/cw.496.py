def nextGreaterElement(nums1: list, nums2: list) -> list:
    result = []
    added = 0

    for num in nums1:
        idx = nums2.index(num)
        for elem in nums2[idx + 1:]:
            if elem > num:
                result.append(elem)
                added = 1
                break
        if added == 0:
            result.append(-1)
        added = 0

    return result


if __name__ == '__main__':
    assert (nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2])) == [-1, 3, -1]
    assert (nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4])) == [3, -1]
