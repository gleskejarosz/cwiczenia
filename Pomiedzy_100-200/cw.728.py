def selfDividingNumbers(left: int, right: int) -> list:
    result = []
    temp = []
    num_list = set()

    for num in range(left, right + 1):
        if str(num).find("0") > 0:
            continue
        if len(str(num)) == 1:
            result.append(num)
            continue
        for elem in str(num):
            if elem != "0":
                num_list.add(elem)
        for n in num_list:
            if num % int(n) == 0:
                temp.append(1)
        if len(num_list) == sum(temp):
            result.append(num)
        num_list = set()
        temp = []

    return result


if __name__ == '__main__':
    assert (selfDividingNumbers(left=9, right=22)) == [9, 11, 12, 15, 22]
    assert (selfDividingNumbers(left=1, right=22)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert (selfDividingNumbers(left=47, right=85)) == [48, 55, 66, 77]
