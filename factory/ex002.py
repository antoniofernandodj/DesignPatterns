from abc import ABC, abstractmethod
from enum import Enum


class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"


class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class Car(Vehicle):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Motorcycle(Vehicle):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Bicycle(Vehicle):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


def create_vehicle(v_type: VehicleType, name: str):
    match v_type:
        case VehicleType.CAR:
            return Car(name)

        case VehicleType.MOTORCYCLE:
            return Motorcycle(name)

        case VehicleType.BICYCLE:
            return Bicycle(name)


bike = create_vehicle(VehicleType.BICYCLE, 'bike')
car = create_vehicle(VehicleType.CAR, 'car')
motorcycle = create_vehicle(VehicleType.MOTORCYCLE, 'motor')
