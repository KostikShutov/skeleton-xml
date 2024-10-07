import xml.etree.ElementTree as ET
from skeleton_xml.command.Command import Command
from skeleton_xml.command.Param import Param


class CommandsParser:
    def __init__(self, root: ET) -> None:
        self.root = root

    def parse(self) -> dict[str, Command]:
        result: dict[str, Command] = {}

        for command in self.root.find('Commands'):
            params: dict[str, Param] = {}

            for param in command.find('Params'):
                paramName: str = param.attrib['name']

                if paramName in params:
                    raise RuntimeError(f'[COMMAND] Command param "{paramName}" already defined')

                params[paramName] = Param(
                    name=paramName,
                )

            commandName: str = command.find('Name').text

            if commandName in result:
                raise RuntimeError(f'[COMMAND] Command "{commandName}" already defined')

            result[commandName] = Command(
                name=commandName,
                params=params,
            )

        return result
