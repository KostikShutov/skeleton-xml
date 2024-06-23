import importlib
import xml.etree.ElementTree as ET
from skeleton_xml.command.Command import Command
from skeleton_xml.command.CommandsParser import CommandsParser
from skeleton_xml.control.Control import Control
from skeleton_xml.control.ControlsParser import ControlsParser
from skeleton_xml.driver.Driver import Driver
from skeleton_xml.driver.DriversParser import DriversParser
from skeleton_xml.interface.Interface import Interface
from skeleton_xml.interface.Inver import Inver
from skeleton_xml.interface.InterfacesParser import InterfacesParser


class ConfigService:
    def __init__(self, config: str):
        root: ET = ET.parse(config).getroot()

        self.commands: dict[str, Command] = CommandsParser(root=root).parse()
        self.controls: dict[str, Control] = ControlsParser(root=root).parse()
        self.drivers: dict[str, Driver] = DriversParser(root=root).parse()
        self.interfaces: dict[str, Interface] = InterfacesParser(root=root).parse()

    def execute(self, commandName: str, request: dict) -> any:
        command: Command = self.__getCommand(commandName=commandName)

        for _, inver in self.__getInvers(commandName=commandName).items():
            driver: Driver = self.__getDriver(inverName=inver.name)
            payload: dict[str, any] = {}

            for paramTo, param in inver.params.items():
                if paramTo not in driver.params:
                    raise RuntimeError(f'Driver parameter "{paramTo}" not available')

                paramFrom: str = param.paramFrom

                if paramFrom not in request:
                    raise RuntimeError(f'Request parameter "{paramFrom}" not passed')

                if paramFrom not in command.params:
                    raise RuntimeError(f'Interface parameter "{paramFrom}" not available')

                payload[paramTo] = request[paramFrom]

            return self.__doExecute(inver=inver, payload=payload)

    def __doExecute(self, inver: Inver, payload: dict[str, any]) -> any:
        driver: Driver = self.__getDriver(inverName=inver.name)
        module, className, method = str.split(driver.module, '/')
        instance: object = getattr(importlib.import_module(module), className)()

        return getattr(instance, method)(**payload)

    def __getCommand(self, commandName: str) -> Command:
        if commandName not in self.commands:
            raise RuntimeError(f'Command "{commandName}" not found')

        return self.commands[commandName]

    def __getInvers(self, commandName: str) -> dict[str, Inver]:
        if commandName not in self.interfaces:
            raise RuntimeError(f'Interface for command "{commandName}" not found')

        return self.interfaces[commandName].invers

    def __getDriver(self, inverName: str) -> Driver:
        if inverName not in self.drivers:
            raise RuntimeError(f'Driver "{inverName}" not found')

        return self.drivers[inverName]
