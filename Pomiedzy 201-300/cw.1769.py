def minOperations(boxes: str) -> list:
    boxes_len = len(boxes)
    result = []
    idx = 0
    moves = 0

    while idx < boxes_len:
        for index, box in enumerate(boxes):
            if idx != index and box == "1":
                moves += abs(idx - index)
        result.append(moves)
        moves = 0
        idx += 1

    return result


if __name__ == '__main__':
    assert (minOperations("110")) == [1, 1, 3]
    assert (minOperations("001011")) == [11, 8, 5, 4, 3, 4]
