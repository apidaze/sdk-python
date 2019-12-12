from lxml import etree


class BaseNode(etree.ElementBase):
    def _init(self):
        self.tag = self.__class__.__name__.lower()

    def bool_value(self, mybool: bool) -> str:
        return 'true' if mybool else 'false'
