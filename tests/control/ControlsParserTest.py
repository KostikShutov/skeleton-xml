import os
import unittest
import xml.etree.ElementTree as ET
from skeleton_xml.control.Control import Control
from skeleton_xml.control.Behaviour import Behaviour
from skeleton_xml.control.ControlsParser import ControlsParser


class ControlsParserTest(unittest.TestCase):
    def setUp(self) -> None:
        path: str = os.path.dirname(os.path.realpath(__file__)) + '/../test.xml'
        root: ET = ET.parse(path).getroot()

        self.controlsParser = ControlsParser(root=root)

    def testParse(self) -> None:
        actual: dict[str, Control] = self.controlsParser.parse()

        self.assertEquals(
            {
                'AUTONOMOUS': Control(
                    name='AUTONOMOUS',
                    module='controls.autonomous',
                    behaviours={
                        'friendly': Behaviour(
                            name='friendly',
                        ),
                        'aggressive': Behaviour(
                            name='aggressive',
                        ),
                    },
                )
            },
            actual,
        )
