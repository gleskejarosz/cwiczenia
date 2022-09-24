def removeDigit(number: str, digit: str) -> str:
    count_d = number.count(digit)

    if count_d == 1:
        return number.replace(digit, "")

    result = [number for x in range(count_d)]

    indexes = []
    for idx, num in enumerate(number):
        if num == digit:
            indexes.append(idx)

    for idx, elem in enumerate(result):
        pos = indexes[idx]
        result[idx] = elem[0: pos] + elem[pos + 1:]

    return max(result)


if __name__ == '__main__':
    assert (removeDigit(number="123", digit="3")) == "12"
    assert (removeDigit(number="1231", digit="1")) == "231"
    assert (removeDigit(number="551", digit="5")) == "51"
