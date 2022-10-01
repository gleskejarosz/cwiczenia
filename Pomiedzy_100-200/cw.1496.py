def isPathCrossing(path: str) -> bool:
    points = [[0, 0], ]

    for idx, elem in enumerate(path):
        x = points[idx][0]
        y = points[idx][1]
        if elem == "N":
            points.append([x, y + 1])
            continue
        if elem == "S":
            points.append([x, y - 1])
            continue
        if elem == "W":
            points.append([x + 1, y])
            continue
        if elem == "E":
            points.append([x - 1, y])
            continue

    for elem in points:
        if points.count(elem) > 1:
            return True
    return False


if __name__ == '__main__':
    assert(isPathCrossing("NES")) is False
    assert(isPathCrossing("NESWW")) is True
