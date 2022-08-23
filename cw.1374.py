def generateTheString(n: int) -> str:

    if n % 2 == 0:
        result = "l" * (n - 1) + "o"
    else:
        result = "l" * n

    return result


if __name__ == '__main__':
    assert(generateTheString(4)) == "lllo"
    assert(generateTheString(2)) == "lo"
    assert(generateTheString(7)) == "lllllll"
