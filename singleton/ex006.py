from threading import Lock


class ThreadingSingleton:

    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance


s1 = ThreadingSingleton()
s2 = ThreadingSingleton()

print(s1 == s2)
