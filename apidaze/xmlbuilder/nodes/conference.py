from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Conference(BaseNode):
    def __init__(self, room: str):
        super().__init__(room)
