import os
import unittest
import xml.etree.ElementTree as ET
from src.command.Command import Command
from src.command.Param import Param
from src.command.CommandsParser import CommandsParser


class CommandsParserTest(unittest.TestCase):
    def setUp(self) -> None:
        path: str = os.path.dirname(os.path.realpath(__file__)) + '/../test.xml'
        root: ET = ET.parse(path).getroot()

        self.commandsParser = CommandsParser(root=root)

    def testParse(self) -> None:
        actual: dict[str, Command] = self.commandsParser.parse()

        self.assertEqual(
            {
                'FORWARD': Command(
                    name='FORWARD',
                    params={
                        'speed': Param(
                            name='speed',
                        ),
                    },
                ),
            },
            actual,
        )
