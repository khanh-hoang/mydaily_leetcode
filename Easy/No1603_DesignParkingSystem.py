class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space = [big, medium, small]
        
    def addCar(self, carType: int) -> bool:
        self.space[carType-1] -= 1
        return self.space[carType-1] >= 0