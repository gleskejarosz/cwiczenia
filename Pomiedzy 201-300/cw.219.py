def containsNearbyDuplicate(nums: list, k: int) -> bool:
    num_len = len(nums)
    if not nums or num_len == 0:
        return False
    table = {}
    left = 0
    right = 0
    while right < num_len:
        if nums[right] in table:
            return True
        table[nums[right]] = 1
        right += 1
        if right - left == k + 1:
            del table[nums[left]]
            left += 1
    return False


if __name__ == '__main__':
    assert (containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)) is True
    assert (containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)) is True
    assert (containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2)) is False
    