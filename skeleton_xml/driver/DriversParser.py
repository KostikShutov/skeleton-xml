import xml.etree.ElementTree as ET
from skeleton_xml.driver.Driver import Driver
from skeleton_xml.driver.Param import Param


class DriversParser:
    def __init__(self, root: ET) -> None:
        self.root = root

    def parse(self) -> dict[str, Driver]:
        result: dict[str, Driver] = {}

        for driver in self.root.find('Drivers'):
            params: dict[str, Param] = {}

            for param in driver.find('Params'):
                paramName: str = param.attrib['name']

                if paramName in result:
                    raise RuntimeError(f'[DRIVER] Driver param "{paramName}" already defined')

                params[paramName] = Param(
                    name=paramName,
                )

            driverName: str = driver.find('Name').text

            if driverName in result:
                raise RuntimeError(f'[DRIVER] Driver "{driverName}" already defined')

            result[driverName] = Driver(
                name=driverName,
                module=driver.find('Module').text,
                method=driver.find('Method').text,
                params=params,
            )

        return result
