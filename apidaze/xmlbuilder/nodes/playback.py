from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Playback(BaseNode):
    def __init__(self, file: str):
        super().__init__(file)
