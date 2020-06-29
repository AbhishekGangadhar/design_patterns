from abc import ABC, abstractmethod
from structural.bridge.artist import Artist
from structural.bridge.book import Book
from structural.bridge.song import Song


class IMediaResource(ABC):
    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_snippet(self) -> str:
        pass


class BookMediaResource(IMediaResource):
    def __init__(self, book: Book):
        self.book = book

    def get_title(self) -> str:
        return self.book.get_title()

    def get_snippet(self) -> str:
        return self.book.get_summary()


class ArtistMediaResource(IMediaResource):
    def __init__(self, artist: Artist):
        self.artist = artist

    def get_title(self) -> str:
        return self.artist.get_name()

    def get_snippet(self) -> str:
        return self.artist.get_biography()


class SongMediaResource(IMediaResource):
    def __init__(self, song: Song):
        self.song = song

    def get_title(self) -> str:
        return self.song.get_name()

    def get_snippet(self) -> str:
        return self.song.get_description()
