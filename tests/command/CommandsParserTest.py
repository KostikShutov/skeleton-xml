import os
import unittest
import xml.etree.ElementTree as ET
from skeleton_xml.command.Command import Command
from skeleton_xml.command.Param import Param
from skeleton_xml.command.CommandsParser import CommandsParser


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
                        'speedFrom': Param(
                            name='speedFrom',
                        ),
                    },
                ),
                'BACKWARD': Command(
                    name='BACKWARD',
                    params={},
                ),
                'STOP': Command(
                    name='STOP',
                    params={},
                ),
                'SECOND_STOP': Command(
                    name='SECOND_STOP',
                    params={},
                ),
                'ZERO': Command(
                    name='ZERO',
                    params={},
                ),
                'TURN': Command(
                    name='TURN',
                    params={},
                ),
            },
            actual,
        )
