def finalValueAfterOperations(operations):
    dict_oper = {"++X": 1,
                 "X++": 1,
                 "--X": -1,
                 "X--": -1}
    result = 0

    for operation in operations:
        result += dict_oper[operation]

    return result


if __name__ == '__main__':
    assert(finalValueAfterOperations(["--X", "X++", "X++"])) == 1
    assert(finalValueAfterOperations(["++X", "++X", "X++"])) == 3
