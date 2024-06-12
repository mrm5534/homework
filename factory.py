from builder import Node
class StyleFactory:
    """风格工厂的基类"""
    def create_root(self, data):
        """创建根节点"""
        raise NotImplementedError("Subclass must implement abstract method")

    def create_node(self, data):
        """创建普通节点"""
        raise NotImplementedError("Subclass must implement abstract method")

class DefaultStyleFactory(StyleFactory):
    """默认风格工厂，例如树状图风格"""
    def create_root(self, data):
        return DefaultNode(data, is_root=True)

    def create_node(self, data):
        return DefaultNode(data)

    def create_tree_structure(self, data_list):
        root = self.create_root(data_list[0])
        current_level = [root]

        for level_data in data_list[1:]:
            next_level = []
            for parent_node, child_data in zip(current_level, level_data):
                child_node = self.create_node(child_data)
                parent_node.add_child(child_node)
                next_level.append(child_node)
            current_level = next_level

        return root

class CustomStyleFactory(StyleFactory):
    """自定义风格工厂，例如矩形布局风格"""
    def create_root(self, data):
        return CustomNode(data, is_root=True)

    def create_node(self, data):
        return CustomNode(data)

class DefaultNode(Node):
    """默认风格的节点"""
    def draw(self):
        print(f"Drawing node with default style: {self.data}")

class CustomNode(Node):
    """自定义风格的节点"""
    def draw(self):
        print(f"Drawing node with custom style: {self.data}")


class TreeStyleFactory(StyleFactory):
    """树状风格工厂，用于生成具有树结构外观的节点"""

    class TreeNode(Node):
        """树状风格的节点，模拟树的外观"""

        def draw(self):
            print(f"Drawing node with tree-style: {self.data}, "
                  f"branching out like a tree!")

    def create_root(self, data):
        """创建具有树状风格的根节点"""
        return self.TreeNode(data, is_root=True)

    def create_node(self, data):
        """创建具有树状风格的普通节点"""
        return self.TreeNode(data)


class RectangleStyleFactory(StyleFactory):
    """矩形风格工厂，用于生成具有矩形布局的节点"""

    class RectangleNode(Node):
        """矩形风格的节点，模拟流程图或组织结构图中的矩形框"""

        def draw(self):
            print(f"Drawing node with rectangle style: {self.data}, "
                  f"boxed in a rectangular shape.")

    def create_root(self, data):
        """创建具有矩形风格的根节点"""
        return self.RectangleNode(data, is_root=True)

    def create_node(self, data):
        """创建具有矩形风格的普通节点"""
        return self.RectangleNode(data)