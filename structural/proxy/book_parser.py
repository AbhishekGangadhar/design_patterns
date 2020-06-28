from abc import ABC, abstractmethod


class IBookParser(ABC):
    @abstractmethod
    def get_total_number_of_words(self) -> int:
        pass


class BookParser(IBookParser):
    def __init__(self, book_text: str):
        self.book_text = book_text
        # Assuming that the below operation is very expensive
        self.total_number_of_words = len(self.book_text.split(" "))

    def get_total_number_of_words(self) -> int:
        return self.total_number_of_words

