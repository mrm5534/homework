from enum import Enum
import json
import argparse
from abc import ABC, abstractmethod
from typing import Any




# Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_dict_node(self, key: str) -> str:
        pass

    @abstractmethod
    def visit_leaf_node(self, key: str, value: Any) -> str:
        pass


# Concrete Visitors integrated with Styles (to avoid redundant visitor creation)
class BaseStyle(ABC):
    def __init__(self, icon_type: 'IconType'):
        self.icons = icon_type.value

    @abstractmethod
    def render_dict_node(self, key: str, level: int) -> str:
        pass

    @abstractmethod
    def render_leaf_node(self, key: str, value: Any, level: int) -> str:
        pass

    def traverse(self, json_data: dict, level: int = 0) -> str:
        result = ""
        indent = "|  " * level
        for key, value in json_data.items():
            if isinstance(value, dict):
                result += f"{indent}{'├─' if level < 1 else '└─'}-{self.render_dict_node(key, level)}"
                result += self.traverse(value, level + 1)
            else:
                result += f"{indent}{'├─' if level < 1 else '└─'}-{self.render_leaf_node(key, value, level)}"
        return result


class TreeStyle(BaseStyle):
    def render_dict_node(self, key: str, level: int) -> str:
        return f"{self.icons[0]}{key}\n"

    def render_leaf_node(self, key: str, value: Any, level: int) -> str:
        return f"{self.icons[1]}{key}: {value}\n"


class RectangleStyle(BaseStyle):
    def render_dict_node(self, key: str, level: int) -> str:
        return f"{self.icons[0]}-{key}{'-' * 30}┐\n"

    def render_leaf_node(self, key: str, value: Any, level: int) -> str:
        return f"{self.icons[1]}{key}: {value}-{'-' * 30}┤\n"


# Icons as Enum for simplicity
class NiceIcon:
    def __str__(self):
        return "♢"


class StarIcon:
    def __str__(self):
        return "★"
class IconType(Enum):
    NICE = (NiceIcon(), NiceIcon())
    STAR = (StarIcon(), StarIcon())





# Simplified Icon retrieval
def get_icon(icon_name: str) -> IconType:
    icons = {
        'nice': IconType.NICE,
        'star': IconType.STAR,
    }
    try:
        return icons[icon_name]
    except KeyError:
        raise ValueError(f"未知图标类型: {icon_name}")


# ...������ԭ�е������н������֣�
# Command Line Parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', type=str, required=True, choices=['tree', 'rectangle'], help='tree or rectangle')
    parser.add_argument('-i', '--icon', type=str, required=True, choices=['nice', 'star'], help='nice or star')
    return parser.parse_args()

# Utility Functions
def get_jsonfile(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
# Main Execution with streamlined logic
def main():
    args = parse_arguments()
    try:
        json_data = get_jsonfile(args.file)
        icon_type = get_icon(args.icon)

        if args.style == 'tree':
            style = TreeStyle(icon_type)
        elif args.style == 'rectangle':
            style = RectangleStyle(icon_type)
        else:
            raise ValueError(f"未知样式: {args.style}")

        result = style.traverse(json_data)
        print(result)
    except FileNotFoundError:
        print(f"错误：文件 {args.file} 未找到。")
    except ValueError as e:
        print(f"配置错误{e}")


if __name__ == "__main__":
    main()