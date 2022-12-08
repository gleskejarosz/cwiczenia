def isHappy(n):
    numbers = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in numbers:
            return False
        else:
            numbers.add(n)
    else:
        return True


if __name__ == '__main__':
    assert(isHappy(1)) is True
    assert(isHappy(2)) is False
    assert(isHappy(19)) is True
