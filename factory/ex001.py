from abc import ABC, abstractmethod
from enum import Enum


# Step 0: Create an enumeration for vehicle types
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"


# Step 1: Create an abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


# Step 2: Create concrete vehicle classes
class Car(Vehicle):
    def __init__(self, name):
        self._name = name

    # Implement the get_name() method
    def get_name(self):
        return self._name


class Motorcycle(Vehicle):
    def __init__(self, name):
        self._name = name

    # Implement the get_name() method
    def get_name(self):
        return self._name


class Bicycle(Vehicle):
    def __init__(self, name):
        self._name = name

    # Implement the get_name() method
    def get_name(self):
        return self._name


# Step 3: Create a VehicleFactory class
class VehicleFactory:
    def create_vehicle(self, vehicle_type: VehicleType) -> Vehicle:
        if vehicle_type == VehicleType.CAR:
            return Car(VehicleType.CAR.value)
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle(VehicleType.MOTORCYCLE.value)
        elif vehicle_type == VehicleType.BICYCLE:
            return Bicycle(VehicleType.BICYCLE.value)
        else:
            raise NotImplementedError


# Step 4: Test the VehicleFactory class
def main():
    vehicle_factory = VehicleFactory()

    # Test the VehicleFactory by creating different types of vehicles
    car = vehicle_factory.create_vehicle(VehicleType.CAR)
    print(car.get_name())

    motorcycle = vehicle_factory.create_vehicle(VehicleType.MOTORCYCLE)
    print(motorcycle.get_name())

    bicycle = vehicle_factory.create_vehicle(VehicleType.BICYCLE)
    print(bicycle.get_name())


if __name__ == "__main__":
    main()
