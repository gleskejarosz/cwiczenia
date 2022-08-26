def digitCount(num: str) -> bool:
    num_list = list(num)

    for pos in range(len(num)):
        if int(num_list[pos]) != num_list.count(str(pos)):
            return False
    return True


if __name__ == '__main__':
    assert(digitCount("1210")) is True
    assert(digitCount("030")) is False
