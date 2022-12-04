def commonFactors(a: int, b: int) -> int:
    s_int = min(a, b)
    counter = 0
    a_factors = []

    for i in range(1, s_int + 1):
        if a % i == 0:
            a_factors.append(i)

    for num in a_factors:
        if b % num == 0:
            counter += 1

    return counter


if __name__ == '__main__':
    assert (commonFactors(a=12, b=6)) == 4
    assert (commonFactors(a=25, b=30)) == 2
