import importlib
import xml.etree.ElementTree as ET
from pathlib import Path
from skeleton_xml.algorithm.Algorithm import Algorithm
from skeleton_xml.algorithm.AlgorithmsParser import AlgorithmsParser
from skeleton_xml.command.Command import Command
from skeleton_xml.command.CommandsParser import CommandsParser
from skeleton_xml.driver.Driver import Driver
from skeleton_xml.driver.DriversParser import DriversParser
from skeleton_xml.interface.Interface import Interface
from skeleton_xml.interface.Inver import Inver
from skeleton_xml.interface.InterfacesParser import InterfacesParser


class ConfigService:
    def __init__(self, config: str):
        root: ET = ET.parse(config).getroot()

        self.algorithms: dict[str, Algorithm] = AlgorithmsParser(root=root).parse()
        self.commands: dict[str, Command] = CommandsParser(root=root).parse()
        self.drivers: dict[str, Driver] = DriversParser(root=root).parse()
        self.interfaces: dict[str, Interface] = InterfacesParser(root=root).parse()

    def execute(self, algorithmName: str, commandName: str, request: dict) -> any:
        algorithm: Algorithm = self.__getAlgorithm(algorithmName=algorithmName)
        command: Command = self.__getCommand(commandName=commandName)

        if commandName not in algorithm.commands:
            raise RuntimeError(f'[REQUEST] Command "{commandName}" not available for algorithm "{algorithmName}"')

        for _, inver in self.__getInvers(commandName=commandName).items():
            driver: Driver = self.__getDriver(inverName=inver.name)
            payload: dict[str, any] = {}

            for paramTo, param in inver.params.items():
                if paramTo not in driver.params:
                    raise RuntimeError(f'[CONFIG] To parameter "{paramTo}" for driver "{driver.name}" not found')

                paramFrom: str = param.paramFrom

                if paramFrom not in command.params:
                    raise RuntimeError(f'[CONFIG] From parameter "{paramFrom}" for command "{commandName}" not found')

                if paramFrom not in request:
                    raise RuntimeError(f'[REQUEST] From parameter "{paramFrom}" for command "{commandName}" not passed')

                payload[paramTo] = request[paramFrom]

            return self.__doExecute(driver=driver, payload=payload)

    def __doExecute(self, driver: Driver, payload: dict[str, any]) -> any:
        path: Path = Path(driver.module)
        extension: str = path.suffix

        if extension == '.py':
            module: str = str(path.with_suffix('')).replace('/', '.')
            className: str = path.stem
            instance: object = getattr(importlib.import_module(module), className)()

            return getattr(instance, driver.method)(**payload)

        raise RuntimeError(f'[CONFIG] Extension "{extension}" not implemented')

    def __getAlgorithm(self, algorithmName: str) -> Algorithm:
        if algorithmName not in self.algorithms:
            raise RuntimeError(f'[REQUEST] Algorithm "{algorithmName}" not found')

        return self.algorithms[algorithmName]

    def __getCommand(self, commandName: str) -> Command:
        if commandName not in self.commands:
            raise RuntimeError(f'[REQUEST] Command "{commandName}" not found')

        return self.commands[commandName]

    def __getInvers(self, commandName: str) -> dict[str, Inver]:
        if commandName not in self.interfaces:
            raise RuntimeError(f'[CONFIG] Interface for command "{commandName}" not found')

        return self.interfaces[commandName].invers

    def __getDriver(self, inverName: str) -> Driver:
        if inverName not in self.drivers:
            raise RuntimeError(f'[CONFIG] Driver "{inverName}" not found')

        return self.drivers[inverName]
