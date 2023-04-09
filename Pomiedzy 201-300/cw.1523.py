def countOdds(low: int, high: int) -> int:
    counter = (high - low) // 2

    if low % 2 == 0 and high % 2 == 1:
        counter += 1
    if low % 2 == 1 and high % 2 == 0:
        counter += 1
    if low % 2 == 1 and high % 2 == 1:
        counter += 1
    return counter


if __name__ == '__main__':
    assert (countOdds(low=3, high=7)) == 3
    assert (countOdds(low=8, high=10)) == 1
