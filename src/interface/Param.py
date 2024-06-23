class Param:
    def __init__(self, paramFrom: str, paramTo: str) -> None:
        self.paramFrom = paramFrom
        self.paramTo = paramTo

    def __eq__(self, other) -> bool:
        return self.paramFrom == other.paramFrom \
            and self.paramTo == other.paramTo

    def __repr__(self) -> str:
        return '(' + str(self.paramFrom) \
            + ', ' + str(self.paramTo) \
            + ')'

    def __str__(self) -> str:
        return '(paramFrom: ' + str(self.paramFrom) \
            + ', paramTo: ' + str(self.paramTo) \
            + ')'
