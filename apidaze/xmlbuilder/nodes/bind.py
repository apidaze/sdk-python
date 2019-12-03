from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Bind(BaseNode):
    def __init__(
            self,
            text: str,
            action: str
            ):
        attrib = {
            'action': action,
        }
        super().__init__(text, attrib=attrib)
