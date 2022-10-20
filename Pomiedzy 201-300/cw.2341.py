def numberOfPairs(nums: list) -> list:
    counter = 0
    possible_pairs = 0

    num_dict = {k: nums.count(k) for k in nums}

    for elem in num_dict:
        count_elem = num_dict[elem]
        left = count_elem % 2
        pairs = count_elem // 2
        possible_pairs += pairs
        counter += left

    return [possible_pairs, counter]


if __name__ == '__main__':
    assert (numberOfPairs([1, 3, 2, 1, 3, 2, 2])) == [3, 1]
    assert (numberOfPairs([1, 1])) == [1, 0]
    assert (numberOfPairs([0])) == [0, 1]
