def divisorGame(n: int) -> bool:
    counter = 0

    while n > 1:
        n = n - 1
        counter += 1
        # if n % 2 == 0:
        #     n = n / 2
        #     counter += 1
        # else:
        #     n = n - 1
        #     counter += 1

    if counter % 2 == 0:
        return False
    return True


if __name__ == '__main__':
    assert(divisorGame(50)) is True
    assert(divisorGame(2)) is True
    assert(divisorGame(3)) is False
    assert(divisorGame(4)) is True
