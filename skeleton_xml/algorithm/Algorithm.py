class Algorithm:
    def __init__(self, name: str, module: str, method: str) -> None:
        self.name = name
        self.module = module
        self.method = method

    def __eq__(self, other) -> bool:
        return self.name == other.name \
            and self.module == other.module \
            and self.method == other.method

    def __repr__(self) -> str:
        return '(' + str(self.name) \
            + ', ' + str(self.module) \
            + ', ' + str(self.method) \
            + ')'

    def __str__(self) -> str:
        return '(name: ' + str(self.name) \
            + ', module: ' + str(self.module) \
            + ', method: ' + str(self.method) \
            + ')'
