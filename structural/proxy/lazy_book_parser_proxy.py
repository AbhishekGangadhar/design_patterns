from structural.proxy.book_parser import IBookParser, BookParser


class LazyBookParserProxy(IBookParser):
    def __init__(self, book_text: str):
        self.book_text = book_text
        self.book_parser = None

    def get_total_number_of_words(self) -> int:
        if self.book_parser is None:
            self.book_parser = BookParser(self.book_text)
        return self.book_parser.get_total_number_of_words()
