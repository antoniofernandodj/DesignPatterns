class ClassicSingleton:
    _instance = None
    a = None
    b = None

    def __init__(self):
        raise RuntimeError('Execute instance() ao invés disso')

    @classmethod
    def get_instance(cls, a, b):
        print('Gettings instance...')
        if not cls._instance:
            cls._instance = cls.__new__(cls)
            cls._instance.a = a
            cls._instance.b = b

        instance = cls._instance
        print('Got instance %s...' % instance)
        return cls._instance


if __name__ == "__main__":
    c1 = ClassicSingleton.get_instance(1, 2)
    c2 = ClassicSingleton.get_instance(3, 4)

    print(c1 is c2)
    print(c1.a == c2.a)
    print(c1.b == c2.b)
