class ParkingSystem:
    def __init__(self, big, medium, small):
        self.A = [big, medium, small]

    def addCar(self, carType):
        self.A[carType - 1] -= 1
        return self.A[carType - 1] >= 0


if __name__ == '__main__':
    parkingSystem = ParkingSystem(1, 1, 0)
    assert(parkingSystem.addCar(1)) is True
    assert(parkingSystem.addCar(2)) is True
    assert(parkingSystem.addCar(3)) is False
    assert(parkingSystem.addCar(1)) is False
