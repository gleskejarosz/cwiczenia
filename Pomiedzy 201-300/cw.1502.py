def canMakeArithmeticProgression(arr: list) -> bool:
    if len(arr) == 2:
        return True

    sorted_arr = sorted(arr)

    diff = sorted_arr[1] - sorted_arr[0]

    for i in range(1, len(arr)):
        if sorted_arr[i] - sorted_arr[i - 1] != diff:
            return False

    return True


if __name__ == '__main__':
    assert (canMakeArithmeticProgression([3, 5])) is True
    assert (canMakeArithmeticProgression([3, 5, 1])) is True
    assert (canMakeArithmeticProgression([1, 2, 4])) is False
