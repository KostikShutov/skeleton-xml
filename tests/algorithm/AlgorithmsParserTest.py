import os
import unittest
import xml.etree.ElementTree as ET
from skeleton_xml.algorithm.Algorithm import Algorithm
from skeleton_xml.algorithm.Command import Command
from skeleton_xml.algorithm.AlgorithmsParser import AlgorithmsParser


class AlgorithmsParserTest(unittest.TestCase):
    def setUp(self) -> None:
        path: str = os.path.dirname(os.path.realpath(__file__)) + '/../test.xml'
        root: ET = ET.parse(path).getroot()

        self.algorithmsParser = AlgorithmsParser(root=root)

    def testParse(self) -> None:
        actual: dict[str, Algorithm] = self.algorithmsParser.parse()

        self.assertEqual(
            {
                'MANUAL': Algorithm(
                    name='MANUAL',
                    commands={
                        'FORWARD': Command(
                            name='FORWARD',
                        ),
                    },
                ),
            },
            actual,
        )
