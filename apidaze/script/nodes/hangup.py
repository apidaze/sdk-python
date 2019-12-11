from apidaze.script.nodes.base_node import BaseNode


class Hangup(BaseNode):
    """
    Hangup the call immediately. Important note : when a call is not
    explicitly hung up, APIdaze will ask for more XML instructions
    by re-fetching the URL of the external script in case the last instruction
    has been processed.

    Returns
    -------
    object
        Hangup node object
    """
    def __init__(self):
        super().__init__()
