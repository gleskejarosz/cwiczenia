def merge(nums1: list, m: int, nums2: list, n: int) -> list:
    """
        Do not return anything, modify nums1 in-place instead.
        """
    nums1[m:] = nums2

    return sorted(nums1)


if __name__ == '__main__':
    assert (merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)) == [1, 2, 2, 3, 5, 6]
    assert (merge(nums1=[1], m=1, nums2=[], n=0)) == [1]
    assert (merge(nums1=[0], m=0, nums2=[1], n=1)) == [1]
