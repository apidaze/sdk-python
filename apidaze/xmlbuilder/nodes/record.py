from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Record(BaseNode):
    """
    Record the call.

    Parameters
    ----------
    name: str
        The name you want to give to your recording file.
        NOTE: There is no suffix in your filename, it is
        automatically suffixed with ".wav". Default is UUID of call.
    on_answered: bool
        Starts recording when the call is answered.
    aleg: bool
        Record the A-leg of the call.. caller to callee.
    bleg: bool
        Record the B-leg of the call.. callee to caller.

    Returns
    -------
    object
        Record node object
    """
    def __init__(
            self,
            name: str = None,
            on_answered: bool = False,
            aleg: bool = True,
            bleg: bool = True):
        attrib = {
            'on-answered': self.bool_value(mybool=on_answered),
            'aleg': self.bool_value(mybool=aleg),
            'bleg': self.bool_value(mybool=bleg)
        }
        if name:
            attrib.update({
                'name': name
            })
        super().__init__(attrib=attrib)
