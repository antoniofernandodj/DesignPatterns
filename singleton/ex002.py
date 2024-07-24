class Singleton:
    _instance = None
    a = None
    b = None

    def __new__(cls, a, b):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.a = a
            cls._instance.b = b

        return cls._instance


if __name__ == "__main__":
    c1 = Singleton(1, 2)
    c2 = Singleton(3, 4)

    print(c1 is c2)
    print(c1.a == c2.a)
    print(c1.b == c2.b)
