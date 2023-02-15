def summaryRanges(nums: list) -> list:
    result = []
    end = ""
    if not nums:
        return []
    prev_num = nums[0]
    start = str(prev_num)
    check = 1

    for num in nums[1:]:
        if num - prev_num > 1:
            if end == "":
                result.append(str(prev_num))
                check = 1
            else:
                result.append(start + "->" + end)
                end = ""
                check = 1
            prev_num = num
            start = str(prev_num)
        else:
            prev_num = num
            end = str(num)
            check = 2

    if check == 1:
        result.append(str(prev_num))

    if check == 2:
        result.append(start + "->" + end)

    return result


if __name__ == '__main__':
    assert (summaryRanges([1, 3])) == ["1", "3"]
    assert (summaryRanges([])) == []
    assert (summaryRanges([0, 1, 2, 4, 5, 7])) == ["0->2", "4->5", "7"]
    assert (summaryRanges([0, 2, 3, 4, 6, 8, 9])) == ["0", "2->4", "6", "8->9"]
