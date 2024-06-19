from style import Style, TreeStyle, RectStyle
from icons import IconFamily, PokerIcons, OtherIcons

class JSONExplorer:
    def __init__(self, style, icon_family):
        self.style = style
        self.icon_family = icon_family

    def render(self, json_data):
        return self.style.render(json_data, self.icon_family)