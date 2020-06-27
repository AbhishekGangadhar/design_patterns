from behavioral.command.command import ICommand


class Invoker:
    def __init__(self):
        self.command_history_stack = []

    def perform_command(self, command: ICommand):
        command.execute()
        self.command_history_stack.append(command)

    def rollback_all_commands(self):
        while len(self.command_history_stack) > 0:
            command = self.command_history_stack.pop()
            command.unexecute()

