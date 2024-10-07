import os
import unittest
from skeleton_xml.ConfigService import ConfigService


class ConfigServiceTest(unittest.TestCase):
    def testOk(self) -> None:
        actual: int = self.__createConfigService('test.xml').execute(
            algorithmName='MANUAL',
            commandName='FORWARD',
            request={
                'speedFrom': 33,
            },
        )

        self.assertEqual(33, actual)

    def testAlgorithmNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').execute(
                algorithmName='NOT_FOUND',
                commandName='FORWARD',
                request={},
            )

        self.assertTrue('[REQUEST] Algorithm "NOT_FOUND" not found' == str(context.exception), context.exception)

    def testCommandNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').execute(
                algorithmName='MANUAL',
                commandName='NOT_FOUND',
                request={},
            )

        self.assertTrue('[REQUEST] Command "NOT_FOUND" not found' == str(context.exception), context.exception)

    def testCommandNotAvailableForAlgorithm(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').execute(
                algorithmName='EMPTY',
                commandName='FORWARD',
                request={},
            )

        self.assertTrue('[REQUEST] Command "FORWARD" not available for algorithm "EMPTY"' == str(context.exception),
                        context.exception)

    def testInterfaceNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').execute(
                algorithmName='EMPTY',
                commandName='ZERO',
                request={},
            )

        self.assertTrue('[CONFIG] Interface for command "ZERO" not found' == str(context.exception), context.exception)

    def testDriverNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').execute(
                algorithmName='MANUAL',
                commandName='BACKWARD',
                request={},
            )

        self.assertTrue('[CONFIG] Driver "NOT_FOUND" not found' == str(context.exception), context.exception)

    def testParamToNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').execute(
                algorithmName='MANUAL',
                commandName='STOP',
                request={},
            )

        self.assertTrue('[CONFIG] To parameter "notFoundTo" for driver "MOTOR" not found' == str(context.exception),
                        context.exception)

    def testParamFromNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').execute(
                algorithmName='MANUAL',
                commandName='SECOND_STOP',
                request={},
            )

        self.assertTrue(
            '[CONFIG] From parameter "notFoundFrom" for command "SECOND_STOP" not found' == str(context.exception),
            context.exception)

    def testParamNotPassed(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').execute(
                algorithmName='MANUAL',
                commandName='FORWARD',
                request={},
            )

        self.assertTrue(
            '[REQUEST] From parameter "speedFrom" for command "FORWARD" not passed' == str(context.exception),
            context.exception)

    def __createConfigService(self, file: str) -> ConfigService:
        path: str = os.path.dirname(os.path.realpath(__file__)) + '/' + file

        return ConfigService(config=path)
