def maximumUnits(boxTypes: list, truckSize: int) -> int:
    units = 0
    sorted_boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)

    for elem in sorted_boxes:
        boxes = elem[0]
        capacity = truckSize - boxes
        if capacity > 0:
            units += boxes * elem[1]
        if capacity == 0:
            units += boxes * elem[1]
            break
        if capacity < 0:
            if truckSize > 0:
                units += truckSize * elem[1]
        truckSize -= boxes

    return units


if __name__ == '__main__':
    assert (maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4)) == 8
    assert (maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10)) == 91
    assert (maximumUnits(boxTypes=[[4, 2], [5, 5], [4, 1], [1, 4], [2, 5], [1, 3], [5, 3], [1, 5], [5, 5], [1, 1]],
                         truckSize=24)) == 95
