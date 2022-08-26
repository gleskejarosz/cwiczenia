def squareIsWhite(coordinates: str) -> bool:
    letters = ["a", "c", "e", "g"]

    if coordinates[0] in letters:
        if int(coordinates[1]) % 2 == 0:
            return True
        else:
            return False
    else:
        if int(coordinates[1]) % 2 == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    assert(squareIsWhite("a1")) is False
    assert(squareIsWhite("h3")) is True
    assert(squareIsWhite("c7")) is False
