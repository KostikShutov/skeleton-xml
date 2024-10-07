from skeleton_xml.algorithm.Command import Command


class Algorithm:
    def __init__(self, name: str, commands: dict[str, Command]) -> None:
        self.name = name
        self.commands = commands

    def __eq__(self, other) -> bool:
        return self.name == other.name \
            and self.commands == other.commands

    def __repr__(self) -> str:
        return '(' + str(self.name) \
            + ', ' + str(self.commands) \
            + ')'

    def __str__(self) -> str:
        return '(name: ' + str(self.name) \
            + ', commands: ' + str(self.commands) \
            + ')'
