import os
import unittest
import xml.etree.ElementTree as ET
from src.driver.Driver import Driver
from src.driver.Param import Param
from src.driver.DriversParser import DriversParser


class DriversParserTest(unittest.TestCase):
    def setUp(self):
        path: str = os.path.dirname(os.path.realpath(__file__)) + '/../test.xml'
        root: ET = ET.parse(path).getroot()

        self.driversParser = DriversParser(root=root)

    def testParser(self) -> None:
        actual: dict[str, Driver] = self.driversParser.parse()

        self.assertEqual(
            {
                'MOTOR': Driver(
                    name='MOTOR',
                    module='drivers.motor',
                    params={
                        'speed': Param(
                            name='speed',
                        ),
                    }
                )
            },
            actual,
        )
