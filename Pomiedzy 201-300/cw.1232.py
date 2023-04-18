def checkStraightLine(coordinates: list) -> bool:
    top = coordinates[1][1] - coordinates[0][1]
    bottom = coordinates[1][0] - coordinates[0][0]
    if bottom == 0:
        a = 0
    else:
        a = top / bottom

    b = coordinates[0][1] - a * coordinates[0][0]

    for coordinate in coordinates:
        x = coordinate[0]
        y = coordinate[1]
        if bottom == 0:
            if x != coordinates[0][0]:
                return False
        elif top == 0:
            if y != coordinates[0][1]:
                return False
        else:
            if y != a * x + b:
                return False

    return True


if __name__ == '__main__':
    assert (checkStraightLine([[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]])) is True
    assert (checkStraightLine([[0, 1], [1, 1], [4, 1]])) is True
    assert (checkStraightLine([[2, 4], [2, 5], [2, 8]])) is True
    assert (checkStraightLine([[0, 0], [0, 1], [0, -1]])) is True
    assert (checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])) is True
    assert (checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])) is False
