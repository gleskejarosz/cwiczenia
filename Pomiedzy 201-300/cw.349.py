def intersection(nums1: list, nums2: list) -> list:
    result = []
    nums1_set = set(nums1)

    for elem in nums1_set:
        if elem in nums2:
            result.append(elem)

    return result


if __name__ == '__main__':
    assert (intersection(nums1=[1, 2, 2, 1], nums2=[2, 2])) == [2]
    assert (intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])) == [9, 4]
