from apidaze.script.nodes.base_node import BaseNode


class Answer(BaseNode):
    """
    Answer the call immediately. Useful if your want to play a sound file
    using the playback tag.

    Returns
    -------
    object
        Answer node object
    """
    def __init__(self):
        super().__init__()
