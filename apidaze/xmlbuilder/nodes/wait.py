from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Wait(BaseNode):
    """
        Delay in seconds
    """
    def __init__(self, delay: int):
        super().__init__(str(delay))
