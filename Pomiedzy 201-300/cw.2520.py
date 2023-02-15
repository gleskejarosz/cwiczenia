def countDigits(num: int) -> int:
    digits = [x for x in str(num)]
    counter = 0

    for digit in digits:
        if num % int(digit) == 0:
            counter += 1

    return counter


if __name__ == '__main__':
    assert(countDigits(7)) == 1
    assert(countDigits(121)) == 2
    assert(countDigits(1248)) == 4
