def numberOfSteps(num: int) -> int:
    steps = 0

    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps += 1

    return steps


if __name__ == '__main__':
    assert(numberOfSteps(14)) == 6
    assert(numberOfSteps(8)) == 4
    assert(numberOfSteps(123)) == 12
