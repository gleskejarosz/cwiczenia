def nearestValidPoint(x: int, y: int, points: list) -> int:
    manhattan_dist = []
    indexes = []

    for idx, point in enumerate(points):
        if point[0] == x or point[1] == y:
            manhattan_dist_elem = abs(point[0] - x) + abs(point[1] - y)
            manhattan_dist.append(manhattan_dist_elem)
            indexes.append(idx)

    if len(manhattan_dist) > 0:
        min_dist = min(manhattan_dist)
        min_ind = manhattan_dist.index(min_dist)
        min_idx = indexes[min_ind]
    else:
        return -1
    return min_idx


if __name__ == '__main__':
    assert (nearestValidPoint(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]])) == 2
    assert (nearestValidPoint(x=3, y=4, points=[[3, 4]])) == 0
    assert (nearestValidPoint(x=3, y=4, points=[[2, 3]])) == -1
