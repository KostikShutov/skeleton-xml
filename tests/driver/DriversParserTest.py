import os
import unittest
import xml.etree.ElementTree as ET
from skeleton_xml.driver.Driver import Driver
from skeleton_xml.driver.Param import Param
from skeleton_xml.driver.DriversParser import DriversParser


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
                    module='tests/MotorDriver.py',
                    method='execute',
                    params={
                        'speedTo': Param(
                            name='speedTo',
                        ),
                    },
                ),
                'SERVO': Driver(
                    name='SERVO',
                    module='tests/ServoDriver.php',
                    method='execute',
                    params={},
                ),
            },
            actual,
        )
