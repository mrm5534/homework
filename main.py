import argparse
import json
from builder import JSONBuilder  # 假设builder.py中已经实现了相应逻辑
from factory import DefaultStyleFactory,TreeStyleFactory,RectangleStyleFactory  # 同样假设factory.py已准备就绪

def main(json_file_path, style_factory=DefaultStyleFactory(), icon_family=None):
    # 假设后续逻辑会使用style_factory和icon_family，这里仅示例
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        builder = JSONBuilder(json_data, factory=style_factory)
        root = builder.build()
        print(json.dumps(root.to_json(),indent=2))  # 或者根据实际情况调用相应的展示逻辑

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument("-f", "--file", required=True, help="Path to the JSON file")
    parser.add_argument("-s", "--style", choices=["tree", "rectangle"], default="tree", help="Output style")
    parser.add_argument("-i", "--icon-family", help="Icon family to use for visualization")

    args = parser.parse_args()

    # 根据参数选择风格工厂。这里仅做示例，实际可能需要更复杂的逻辑
    if args.style == "tree":
        style_factory = TreeStyleFactory()  # 假设TreeStyleFactory已定义
    else:  # rectangle
        style_factory = RectangleStyleFactory()  # 同样假设RectangleStyleFactory已定义

    main(args.file, style_factory, args.icon_family)