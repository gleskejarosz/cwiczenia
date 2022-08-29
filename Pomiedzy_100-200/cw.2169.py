def countOperations(num1: int, num2: int) -> int:
    count = 0
    if num1 == 0 or num2 == 0:
        return 0

    while num1 > 0 or num2 > 0:
        if num2 > num1:
            num2 = num2 - num1
        else:
            num1 = num1 - num2
        count += 1
        if num1 == 0 or num2 == 0:
            break

    return count


if __name__ == '__main__':
    assert (countOperations(num1=2, num2=3)) == 3
    assert (countOperations(num1=10, num2=10)) == 1
    assert (countOperations(num1=0, num2=1)) == 0
    assert (countOperations(num1=2, num2=3)) == 3
