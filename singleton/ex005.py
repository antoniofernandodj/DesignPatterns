
from typing import Any, Dict


class SingletonMetaEagerLoading(type):
    _instances: Dict[Any, Any] = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        instance = cls._instances[cls]
        return instance


class SingletonEager(metaclass=SingletonMetaEagerLoading):
    def __init__(self):
        import random
        self.a = random.randint(1, 100)
        self.b = random.randint(1, 100)


c1 = SingletonEager()
c2 = SingletonEager()

print(c1 is c2)
