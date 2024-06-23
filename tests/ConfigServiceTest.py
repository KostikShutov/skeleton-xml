import os
import unittest
from skeleton_xml.ConfigService import ConfigService


class ConfigServiceTest(unittest.TestCase):
    def setUp(self):
        path: str = os.path.dirname(os.path.realpath(__file__)) + '/test.xml'

        self.configService = ConfigService(config=path)

    def testExecute(self) -> None:
        actual: int = self.configService.execute(
            commandName='FORWARD',
            request={
                'speedFrom': 33,
            },
        )

        self.assertEqual(33, actual)
