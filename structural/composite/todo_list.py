from abc import ABC, abstractmethod


class IToDoList(ABC):
    @abstractmethod
    def get_html(self) -> str:
        pass
