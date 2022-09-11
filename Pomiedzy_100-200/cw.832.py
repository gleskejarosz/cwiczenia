def flipAndInvertImage(image: list) -> list:
    image_len = len(image)
    new_image = [[0 for x in range(image_len)] for x in range(image_len)]
    idx = -1

    for index, elem in enumerate(image):
        for num in elem:
            if num == 1:
                new_image[index][idx] = 0
            else:
                new_image[index][idx] = 1
            idx -= 1
        idx = -1

    return new_image


if __name__ == '__main__':
    assert (flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])) == [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert (flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])) == [[1, 1, 0, 0],
                                                                                              [0, 1, 1, 0],
                                                                                              [0, 0, 0, 1],
                                                                                              [1, 0, 1, 0]]
