def largestOddNumber(num: str) -> str:
    result = []
    odd_test = 0

    odds = ["1", "3", "5", "7", "9"]
    for odd in odds:
        if odd in num:
            odd_test += 1

    if odd_test == 0:
        return ""

    i = 0
    j = len(num)
    loop = 1
    while i < j:
        test_num = num[i: j]
        if int(test_num) % 2 == 1:
            result.append(int(test_num))
        if loop % 2 == 1:
            i += 1
        else:
            i -= 1
            j -= 1
        loop += 1
        if len(result) >= 2:
            break

    if not result:
        return ""

    return str(max(result))


if __name__ == '__main__':
    assert(largestOddNumber("52")) == "5"
    assert(largestOddNumber("4206")) == ""
    assert(largestOddNumber("35427")) == "35427"
    assert(largestOddNumber("85432")) == "8543"