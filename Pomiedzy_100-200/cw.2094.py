import copy


def findEvenNumbers(digits: list) -> list:
    integers = set()
    result = []
    digits_2 = copy.deepcopy(digits)
    digits_3 = copy.deepcopy(digits)

    for idx, digit in enumerate(digits):
        if digit == 0:
            continue
        integer = str(digit)
        digits_2.pop(idx)
        digits_3.pop(idx)
        for index, num in enumerate(digits_2):
            integer += str(num)
            digits_3.pop(index)
            for n in digits_3:
                integer += str(n)
                integers.add(int(integer))
                integer = integer[:2]
            integer = integer[0]
            digits_3.insert(index, num)
        digits_2.insert(idx, digit)
        digits_3.insert(idx, digit)

    for num in integers:
        if num % 2 == 0:
            result.append(num)

    return sorted(result)


def findEvenNumbers2(digits: list) -> list:
    digit_list = [x for x in range(100, 1000)]
    result = []
    for digit in digit_list:
        digit_str = str(digit)
        d_first = int(digit_str[0])
        d_second = int(digit_str[1])
        d_third = int(digit_str[2])
        if d_first not in digits:
            continue
        if d_second not in digits:
            continue
        if d_third not in digits:
            continue
        if d_third % 2 == 1:
            continue
        if d_first == d_second:
            if digits.count(d_first) == 1:
                continue
        if d_first == d_third:
            if digits.count(d_first) == 1:
                continue
        if d_third == d_second:
            if digits.count(d_third) == 1:
                continue
        if d_first == d_second and d_second == d_third:
            if digits.count(d_first) < 3:
                continue
        result.append(digit)

    return result


if __name__ == '__main__':
    assert (findEvenNumbers([2, 1, 3, 0])) == [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
    assert (findEvenNumbers([2, 2, 8, 8, 2])) == [222, 228, 282, 288, 822, 828, 882]
    assert (findEvenNumbers([3, 7, 5])) == []
    assert (findEvenNumbers2([2, 1, 3, 0])) == [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
    assert (findEvenNumbers2([2, 2, 8, 8, 2])) == [222, 228, 282, 288, 822, 828, 882]
    assert (findEvenNumbers2([3, 7, 5])) == []
