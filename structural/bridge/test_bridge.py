import unittest
from unittest import TestCase
from structural.bridge.artist import Artist
from structural.bridge.book import Book
from structural.bridge.song import Song

from structural.bridge.view import HorizontalView, VerticalView
from structural.bridge.media_resource import ArtistMediaResource, BookMediaResource, SongMediaResource


class TestBridgePattern(TestCase):
    def test(self):
        artist_media_resource = ArtistMediaResource(Artist("The Guy", "He is a guy who sings", ["album1", "album2"]))
        book_media_resource = BookMediaResource(Book("The Hobbit", "Tale of Bilbo Baggins", "The actual story"))
        song_media_resource = SongMediaResource(Song("Thunder", "Description of the song"))

        horizontal_artist_view = HorizontalView(artist_media_resource)
        horizontal_book_view = HorizontalView(book_media_resource)
        horizontal_song_view = HorizontalView(song_media_resource)
        vertical_artist_view = VerticalView(artist_media_resource)
        vertical_book_view = VerticalView(book_media_resource)
        vertical_song_view = VerticalView(song_media_resource)

        self.assertEqual("The Guy: He is a guy who sings", horizontal_artist_view.show())
        self.assertEqual("The Hobbit: Tale of Bilbo Baggins", horizontal_book_view.show())
        self.assertEqual("Thunder: Description of the song", horizontal_song_view.show())
        self.assertEqual("The Guy\nHe is a guy who sings", vertical_artist_view.show())
        self.assertEqual("The Hobbit\nTale of Bilbo Baggins", vertical_book_view.show())
        self.assertEqual("Thunder\nDescription of the song", vertical_song_view.show())


if __name__ == '__main__':
    unittest.main()
