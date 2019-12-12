from apidaze.script.nodes.base_node import BaseNode


class Echo(BaseNode):
    """
    Echo back received audio to the caller with some delay.

    Parameters
    ----------
    delay: int
        Delay in miliseconds

    Returns
    -------
    object
        Echo node object
    """
    def __init__(self, delay: int = None):
        if delay:
            super().__init__(str(delay))
        else:
            super().__init__()
