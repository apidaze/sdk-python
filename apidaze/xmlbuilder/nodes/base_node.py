from lxml import objectify


class BaseNode(objectify.ObjectifiedElement):
    def bool_value(self, mybool: bool) -> str:
        return 'true' if mybool else'false'
