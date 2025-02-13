class MotorDriver:
    def __init__(self, entry: dict) -> None:
        self.entry = entry

    def executeFirst(self, speedTo: int) -> int:
        return speedTo

    def executeSecond(self, speedTo: int) -> int:
        return speedTo * 2
