from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Record(BaseNode):
    def __init__(
            self,
            name: str,
            on_answered: bool = False,
            aleg: bool = True,
            bleg: bool = True):
        attrib = {
            'name': name,
            'on-answered': self.bool_value(mybool=on_answered),
            'aleg': self.bool_value(mybool=aleg),
            'bleg': self.bool_value(mybool=bleg)
        }
        super().__init__(attrib=attrib)
