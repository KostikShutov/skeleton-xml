from skeleton_xml.command.Param import Param


class Command:
    def __init__(self, name: str, params: dict[str, Param]) -> None:
        self.name = name
        self.params = params

    def __eq__(self, other) -> bool:
        return self.name == other.name \
            and self.params == other.params

    def __repr__(self) -> str:
        return '(' + str(self.name) \
            + ', ' + str(self.params) \
            + ')'

    def __str__(self) -> str:
        return '(name: ' + str(self.name) \
            + ', params: ' + str(self.params) \
            + ')'
