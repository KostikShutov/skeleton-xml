import xml.etree.ElementTree as ET
from skeleton_xml.interface.Interface import Interface
from skeleton_xml.interface.Inver import Inver
from skeleton_xml.interface.Param import Param


class InterfacesParser:
    def __init__(self, root: ET) -> None:
        self.root = root

    def parse(self) -> dict[str, Interface]:
        result: dict[str, Interface] = {}

        for interface in self.root.find('Interfaces'):
            invers: dict[str, Inver] = {}

            for driver in interface.find('Drivers'):
                params: dict[str, Param] = {}

                for param in driver.find('Params'):
                    paramTo: str = param.attrib['paramTo']

                    if paramTo in params:
                        raise RuntimeError(f'[INTERFACE] Param to "{paramTo}" already defined')

                    params[paramTo] = Param(
                        paramFrom=param.attrib['paramFrom'],
                        paramTo=paramTo,
                    )

                inverName: str = driver.attrib['name']

                if inverName in invers:
                    raise RuntimeError(f'[INTERFACE] Inver "{inverName}" already defined')

                invers[inverName] = Inver(
                    name=inverName,
                    params=params,
                )

            commandName: str = interface.find('Command').text

            if commandName in result:
                raise RuntimeError(f'[INTERFACE] Interface for command "{commandName}" already defined')

            result[commandName] = Interface(
                command=commandName,
                invers=invers,
            )

        return result
