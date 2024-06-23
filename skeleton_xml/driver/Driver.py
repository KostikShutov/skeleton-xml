from skeleton_xml.driver.Param import Param


class Driver:
    def __init__(self, name: str, module: str, params: dict[str, Param]) -> None:
        self.name = name
        self.module = module
        self.params = params

    def __eq__(self, other) -> bool:
        return self.name == other.name \
            and self.module == other.module \
            and self.params == other.params

    def __repr__(self) -> str:
        return '(' + str(self.name) \
            + ', ' + str(self.module) \
            + ', ' + str(self.params) \
            + ')'

    def __str__(self) -> str:
        return '(name: ' + str(self.name) \
            + ', module: ' + str(self.module) \
            + ', params: ' + str(self.params) \
            + ')'
