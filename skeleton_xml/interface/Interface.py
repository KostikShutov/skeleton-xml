from skeleton_xml.interface.Inver import Inver


class Interface:
    def __init__(self, command: str, invers: dict[str, Inver]) -> None:
        self.command = command
        self.invers = invers

    def __eq__(self, other) -> bool:
        return self.command == other.command \
            and self.invers == other.invers

    def __repr__(self) -> str:
        return '(' + str(self.command) \
            + ', ' + str(self.invers) \
            + ')'

    def __str__(self) -> str:
        return '(command: ' + str(self.command) \
            + ', invers: ' + str(self.invers) \
            + ')'
