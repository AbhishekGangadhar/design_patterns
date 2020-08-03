from typing import List

from structural.composite.todo_list import IToDoList


class Project(IToDoList):
    def __init__(self, project_name: str, todos: List[IToDoList]):
        self.project_name = project_name
        self.todos = todos

    def get_html(self) -> str:
        html = f"<h1>{self.project_name}</h1>\n"
        html += "<ul>\n"
        for todo in self.todos:
            html += "<li>" + todo.get_html() + "</li>\n"
        html += "</ul>\n"
        return html
