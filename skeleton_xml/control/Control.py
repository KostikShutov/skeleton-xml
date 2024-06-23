from skeleton_xml.control.Behaviour import Behaviour


class Control:
    def __init__(self, name: str, module: str, behaviours: dict[str, Behaviour]) -> None:
        self.name = name
        self.module = module
        self.behaviours = behaviours

    def __eq__(self, other) -> bool:
        return self.name == other.name \
            and self.module == other.module \
            and self.behaviours == other.behaviours

    def __repr__(self) -> str:
        return '(' + str(self.name) \
            + ', ' + str(self.module) \
            + ', ' + str(self.behaviours) \
            + ')'

    def __str__(self) -> str:
        return '(name: ' + str(self.name) \
            + ', module: ' + str(self.module) \
            + ', behaviours: ' + str(self.behaviours) \
            + ')'
