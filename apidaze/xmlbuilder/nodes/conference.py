from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Conference(BaseNode):
    """
    Join an audio conference.

    Parameters
    ----------
    room: str
        Meeting room to join.

    Returns
    -------
    object
        Conference node object
    """
    def __init__(self, room: str):
        super().__init__(room)
