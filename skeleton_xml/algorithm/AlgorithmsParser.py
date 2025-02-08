import xml.etree.ElementTree as ET
from skeleton_xml.algorithm.Algorithm import Algorithm


class AlgorithmsParser:
    def __init__(self, root: ET) -> None:
        self.root = root

    def parse(self) -> dict[str, Algorithm]:
        result: dict[str, Algorithm] = {}

        for algorithm in self.root.find('Algorithms'):
            algorithmName: str = algorithm.find('Name').text

            if algorithmName in result:
                raise RuntimeError(f'[ALGORITHM] Algorithm "{algorithmName}" already defined')

            result[algorithmName] = Algorithm(
                name=algorithmName,
                module=algorithm.find('Module').text,
                method=algorithm.find('Method').text,
            )

        return result
