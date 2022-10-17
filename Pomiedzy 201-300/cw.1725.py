def countGoodRectangles(rectangles: list) -> int:
    largest_squares = []

    for rectangle in rectangles:
        if rectangle[0] > rectangle[1]:
            largest_squares.append(rectangle[1])
        else:
            largest_squares.append(rectangle[0])

    max_len = max(largest_squares)
    counter = largest_squares.count(max_len)

    return counter


if __name__ == '__main__':
    assert (countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]])) == 3
    assert (countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]])) == 3
