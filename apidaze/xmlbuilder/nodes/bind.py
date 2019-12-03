from apidaze.xmlbuilder.nodes.base_node import BaseNode


class Bind(BaseNode):
    """
    Get the digits dialed, and take an action. Digits are accepted,
    and regular expressions too, the XML text must then start with ~.
    The bind tag is a sub-tag of the playback and speak tags.

    NOTE: Once the digits match a bind statement they are passed as URL
    parameter "dialed_digits" to the URL specified in the action attribute
    of your code.

    Parameters
    ----------
    text: str
        Digit or regular expression
    action: str
        The URL to fetch if the digit matches

    Returns
    -------
    object
        Bind node object
    """
    def __init__(
            self,
            text: str,
            action: str
            ):
        attrib = {
            'action': action,
        }
        super().__init__(text, attrib=attrib)
