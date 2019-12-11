from apidaze.script.nodes.base_node import BaseNode


class Wait(BaseNode):
    """
    Suspend the execution for a while

    Parameters
    ----------
    delay: str
        Delay in seconds

    Returns
    -------
    object
        Wait node object
    """
    def __init__(self, delay: int):
        super().__init__(str(delay))
