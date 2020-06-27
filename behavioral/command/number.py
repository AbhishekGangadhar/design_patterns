class Number:
    def __init__(self, number: int):
        self.__number = number

    def get_number(self) -> int:
        return self.__number

    def set_number(self, number: int):
        self.__number = number
