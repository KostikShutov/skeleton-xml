import os
import unittest
import xml.etree.ElementTree as ET
from skeleton_xml.interface.Interface import Interface
from skeleton_xml.interface.Inver import Inver
from skeleton_xml.interface.Param import Param
from skeleton_xml.interface.InterfacesParser import InterfacesParser


class InterfaceParserTest(unittest.TestCase):
    def setUp(self):
        path: str = os.path.dirname(os.path.realpath(__file__)) + '/../test.xml'
        root: ET = ET.parse(path).getroot()

        self.interfacesParser = InterfacesParser(root=root)

    def testParser(self) -> None:
        actual: dict[str, Interface] = self.interfacesParser.parse()

        self.assertEqual(
            {
                'FORWARD': Interface(
                    command='FORWARD',
                    invers={
                        'MOTOR': Inver(
                            name='MOTOR',
                            params={
                                'speedTo': Param(
                                    paramFrom='speedFrom',
                                    paramTo='speedTo',
                                ),
                            }
                        ),
                    }
                )
            },
            actual,
        )
