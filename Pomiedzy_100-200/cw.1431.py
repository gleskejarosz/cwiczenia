def kidsWithCandies(candies: list, extraCandies: int) -> list:
    max_candies = max(candies)
    result = []

    for candy in candies:
        if candy + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)

    return result


if __name__ == '__main__':
    assert (kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3)) == [True, True, True, False, True]
    assert (kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1)) == [True, False, False, False, False]
    assert (kidsWithCandies(candies=[12, 1, 12], extraCandies=10)) == [True, False, True]
