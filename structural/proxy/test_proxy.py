import unittest
from unittest import TestCase
from structural.proxy.book_parser import BookParser
from structural.proxy.lazy_book_parser_proxy import LazyBookParserProxy


class TestProxyPattern(TestCase):
    def test(self):
        sample_text = "This is a sample text"
        book_parser = BookParser(sample_text)
        self.assertEqual(5, book_parser.total_number_of_words)
        self.assertEqual(5, book_parser.get_total_number_of_words())

        lazy_book_parser_proxy = LazyBookParserProxy(sample_text)
        self.assertIs(None, lazy_book_parser_proxy.book_parser)
        self.assertEqual(5, lazy_book_parser_proxy.get_total_number_of_words())


if __name__ == '__main__':
    unittest.main()
