def minOperations(logs: list) -> int:
    counter = 0

    for log in logs:
        if log == "../":
            if counter > 0:
                counter -= 1
        if log[0] != ".":
            counter += 1

    return counter


if __name__ == '__main__':
    assert (minOperations(["d1/", "d2/", "../", "d21/", "./"])) == 2
    assert (minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"])) == 3
    assert (minOperations(["d1/", "../", "../", "../"])) == 0
    assert (minOperations(["./", "wz4/", "../", "mj2/", "../", "../", "ik0/", "il7/"])) == 2
