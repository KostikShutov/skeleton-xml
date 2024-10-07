import xml.etree.ElementTree as ET
from skeleton_xml.algorithm.Algorithm import Algorithm
from skeleton_xml.algorithm.Command import Command


class AlgorithmsParser:
    def __init__(self, root: ET) -> None:
        self.root = root

    def parse(self) -> dict[str, Algorithm]:
        result: dict[str, Algorithm] = {}

        for algorithm in self.root.find('Algorithms'):
            commands: dict[str, Command] = {}

            for command in algorithm.find('Commands'):
                commandName: str = command.text

                if commandName in commands:
                    raise RuntimeError(f'[ALGORITHM] Command "{commandName}" already defined')

                commands[commandName] = Command(
                    name=commandName,
                )

            algorithmName: str = algorithm.find('Name').text

            if algorithmName in result:
                raise RuntimeError(f'[ALGORITHM] Algorithm "{algorithmName}" already defined')

            result[algorithmName] = Algorithm(
                name=algorithmName,
                commands=commands,
            )

        return result
