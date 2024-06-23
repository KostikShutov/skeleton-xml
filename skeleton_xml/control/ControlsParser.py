import xml.etree.ElementTree as ET
from skeleton_xml.control.Control import Control
from skeleton_xml.control.Behaviour import Behaviour


class ControlsParser:
    def __init__(self, root: ET) -> None:
        self.root = root

    def parse(self) -> dict[str, Control]:
        result: dict[str, Control] = {}

        for control in self.root.find('Controls'):
            behaviours: dict[str, Behaviour] = {}

            for behaviour in control.find('Behaviours'):
                behaviourName: str = behaviour.attrib['name']

                if behaviourName in behaviours:
                    raise RuntimeError(f'Behaviour "{behaviourName}" already defined')

                behaviours[behaviourName] = Behaviour(
                    name=behaviourName,
                )

            controlName: str = control.find('Name').text

            if controlName in result:
                raise RuntimeError(f'Control "{controlName}" already defined')

            result[controlName] = Control(
                name=controlName,
                module=control.find('Module').text,
                behaviours=behaviours,
            )

        return result
