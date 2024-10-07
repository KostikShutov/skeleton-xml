class Command:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        return '(' + str(self.name) \
            + ')'

    def __str__(self) -> str:
        return '(name: ' + str(self.name) \
            + ')'
