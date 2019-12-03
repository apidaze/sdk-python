from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Intercept(BaseNode):
    """
    Intercept a channel. The channel is identified by a UUID parameter that
    must have been stored in some way by your script. You can map this
    application with a dialing sequence (e.g. : *8) to implement group-pickup
    or directed-pickup functions.

    Parameters
    ----------
    uuid: str
        UUID of the channel to be intercepted.

    Returns
    -------
    object
        Intercept node object
    """
    def __init__(self, uuid: str):
        super().__init__(uuid)
