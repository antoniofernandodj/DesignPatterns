from typing import List


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)


class Observer:
    def update(self, data):
        pass  # This method will be overridden by concrete observers


# Concrete observer
class ConcreteObserver(Observer):
    def update(self, data):
        print(f"Received data: {data}")


def notify(data, observers: List[Observer]):
    for observer in observers:
        observer.update(data)


# Usage
subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

notify("Data 1", subject._observers)


# Output:
# Received data: Data 1
# Received data: Data 2