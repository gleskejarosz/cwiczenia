def wateringPlants(plants: list, capacity: int) -> int:
    moves = 0
    temp_capacity = capacity
    for idx, plant in enumerate(plants):
        if temp_capacity < plant:
            moves += 2 * idx
            temp_capacity = capacity
        moves += 1
        temp_capacity -= plant
    return moves


if __name__ == '__main__':
    assert (wateringPlants(plants=[2, 2, 3, 3], capacity=5)) == 14
    assert (wateringPlants(plants=[1, 1, 1, 4, 2, 3], capacity=4)) == 30
    assert (wateringPlants(plants=[7, 7, 7, 7, 7, 7, 7], capacity=8)) == 49
