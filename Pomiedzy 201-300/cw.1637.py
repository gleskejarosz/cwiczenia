def maxWidthOfVerticalArea(points: list) -> int:
    widths = []

    sorted_points = sorted(points)

    for idx, point in enumerate(sorted_points):
        if idx == 0:
            continue
        width = point[0] - sorted_points[idx - 1][0]
        widths.append(width)

    return max(widths)


if __name__ == '__main__':
    assert (maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]])) == 1
    assert (maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]])) == 3
