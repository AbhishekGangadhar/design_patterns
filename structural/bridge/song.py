
class Song:
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description
