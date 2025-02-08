import os
import unittest
from skeleton_xml.ConfigService import ConfigService


class ConfigServiceTest(unittest.TestCase):
    def testAlgorithmOk(self) -> None:
        actual: int = self.__createConfigService('test.xml').executeAlgorithm(
            algorithmName='AUTO',
        )

        self.assertEqual(77, actual)

    def testAlgorithmNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').executeAlgorithm(
                algorithmName='NOT_FOUND',
            )

        self.assertTrue('[REQUEST] Algorithm "NOT_FOUND" not found' == str(context.exception), context.exception)

    def testCommandOk(self) -> None:
        actual: list[int] = self.__createConfigService('test.xml').executeCommand(
            commandName='FORWARD',
            request={
                'speedFrom': 33,
            },
        )

        self.assertEqual([33, 66], actual)

    def testCommandNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').executeCommand(
                commandName='NOT_FOUND',
                request={},
            )

        self.assertTrue('[REQUEST] Command "NOT_FOUND" not found' == str(context.exception), context.exception)

    def testInterfaceNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').executeCommand(
                commandName='ZERO',
                request={},
            )

        self.assertTrue('[CONFIG] Interface for command "ZERO" not found' == str(context.exception), context.exception)

    def testDriverNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').executeCommand(
                commandName='BACKWARD',
                request={},
            )

        self.assertTrue('[CONFIG] Driver "NOT_FOUND" not found' == str(context.exception), context.exception)

    def testParamToNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').executeCommand(
                commandName='STOP',
                request={},
            )

        self.assertTrue('[CONFIG] To parameter "notFoundTo" for driver "MOTOR" not found' == str(context.exception),
                        context.exception)

    def testParamFromNotFound(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').executeCommand(
                commandName='SECOND_STOP',
                request={},
            )

        self.assertTrue(
            '[CONFIG] From parameter "notFoundFrom" for command "SECOND_STOP" not found' == str(context.exception),
            context.exception)

    def testParamNotPassed(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').executeCommand(
                commandName='FORWARD',
                request={},
            )

        self.assertTrue(
            '[REQUEST] From parameter "speedFrom" for command "FORWARD" not passed' == str(context.exception),
            context.exception)

    def testExtensionNotImplemented(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.__createConfigService('test.xml').executeCommand(
                commandName='TURN',
                request={},
            )

        self.assertTrue('[CONFIG] Extension ".php" not implemented' == str(context.exception), context.exception)

    def __createConfigService(self, file: str) -> ConfigService:
        path: str = os.path.dirname(os.path.realpath(__file__)) + '/' + file

        return ConfigService(config=path)
