#from factory import StyleFactory, DefaultStyleFactory, CustomStyleFactory

class Node:
    """可视化节点的基础类"""
    def __init__(self, data,children=None, is_root=False):
        self.data = data
        self.children =children if children is not None else []
        self.is_root = is_root

    def add_child(self, child):
        self.children.append(child)

    def to_json(self):
        return {
            'name': self.data,
            'children': [child.to_json() for child in self.children]
        }

    def draw(self):
        """抽象方法，由子类实现具体的绘制逻辑"""
        raise NotImplementedError("Subclass must implement abstract method")

class JSONBuilder:
    """根据JSON数据和指定的风格构建可视化结构"""
    def __init__(self, json_data, factory):
        self.json_data = json_data
        self.factory = factory

    def build(self):
        """构建根节点并递归构建子节点"""
        root_node = self.factory.create_root(self.json_data)
        self._build_children(root_node, self.json_data)
        return root_node

    def _build_children(self, parent_node, children_data):
        """递归构建子节点"""
        for child_data in children_data.get("children", []):
            child_node = self.factory.create_node(child_data)
            parent_node.add_child(child_node)
            self._build_children(child_node, child_data)