from typing import Any, Dict


class SingletonMeta(type):
    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Singleton2(metaclass=SingletonMeta):
    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == "__main__":
    c1 = Singleton2(1, 2)
    c2 = Singleton2(3, 4)

    print(c1 is c2)
    print(c1.a == c2.a)
