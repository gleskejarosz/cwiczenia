def fill(image, sr, sc, color, current):
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
        return
    if current != image[sr][sc]:
        return
    image[sr][sc] = color

    fill(image, sr - 1, sc, color, current)
    fill(image, sr + 1, sc, color, current)
    fill(image, sr, sc - 1, color, current)
    fill(image, sr, sc + 1, color, current)


def floodFill(image: list, sr: int, sc: int, color: int) -> list:
    if image[sr][sc] == color:
        return image

    fill(image, sr, sc, color, image[sr][sc])
    return image


if __name__ == '__main__':
    assert (floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)) == [[2, 2, 2], [2, 2, 0],
                                                                                         [2, 0, 1]]
    assert (floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0)) == [[0, 0, 0], [0, 0, 0]]
