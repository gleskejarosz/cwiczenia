def wateringPlants(plants: list, capacity: int) -> int:
    temp_capacity = capacity
    moves = 1
    idx = 0
    start = 1

    while idx < len(plants):
        plant = plants[idx]
        if plant <= temp_capacity:
            temp_capacity -= plant
            start = 1
            idx += 1
        else:
            moves += idx
            start = 0
            temp_capacity = capacity
        if start == 0:
            moves += idx
        else:
            moves += 1

    return moves - 1


if __name__ == '__main__':
    assert (wateringPlants(plants=[2, 2, 3, 3], capacity=5)) == 14
    assert (wateringPlants(plants=[1, 1, 1, 4, 2, 3], capacity=4)) == 30
    assert (wateringPlants(plants=[7, 7, 7, 7, 7, 7, 7], capacity=8)) == 49
