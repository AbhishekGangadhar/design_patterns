from typing import List


class Artist:
    def __init__(self, name: str, biography: str, albums: List[str] = None):
        self.__name = name
        self.__biography = biography
        self.__albums = albums

    def get_name(self) -> str:
        return self.__name

    def get_biography(self) -> str:
        return self.__biography

    def get_albums(self) -> List[str]:
        return self.__albums
