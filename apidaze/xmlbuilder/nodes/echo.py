from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Echo(BaseNode):
    def __init__(self, delay: int):
        super().__init__(str(delay))
