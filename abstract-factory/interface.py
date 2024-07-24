from abc import ABC, abstractmethod


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> 'Button':
        raise NotImplementedError

    @abstractmethod
    def create_checkbox(self) -> 'Checkbox':
        raise NotImplementedError


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass
