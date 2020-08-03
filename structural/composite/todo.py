from structural.composite.todo_list import IToDoList


class Todo(IToDoList):
    def __init__(self, item: str):
        self.item = item

    def get_html(self) -> str:
        return self.item
