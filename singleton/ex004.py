
from typing import Any, Dict


class SingletonMetaEagerLoading(type):
    _instances: Dict[Any, Any] = {}

    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        cls._instances[new_class] = super(
            SingletonMetaEagerLoading, new_class  # type: ignore
        ).__call__()

        return new_class

    def __call__(cls, *args, **kwargs):
        instance = cls._instances[cls]
        return instance


class SingletonEager(metaclass=SingletonMetaEagerLoading):
    def __init__(self):
        import random
        self.a = random.randint(1, 100)
        self.b = random.randint(1, 100)


if __name__ == "__":
    c1 = SingletonEager()
    c2 = SingletonEager()

    print(c1 is c2)
