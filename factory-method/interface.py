from abc import ABC, abstractmethod


class DocumentFactory(ABC):
    @abstractmethod
    def create_page(self) -> 'Page':
        raise NotImplementedError


class Page(ABC):
    @abstractmethod
    def describe(self):
        pass
