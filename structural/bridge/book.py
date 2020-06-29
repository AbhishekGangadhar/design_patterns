
class Book:
    def __init__(self, title: str, summary: str, content: str):
        self.__title = title
        self.__summary = summary
        self.__content = content

    def get_title(self) -> str:
        return self.__title

    def get_summary(self) -> str:
        return self.__summary

    def get_content(self) -> str:
        return self.__content
