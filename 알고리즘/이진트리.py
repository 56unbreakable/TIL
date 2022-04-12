# 노드 구현
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 이진 트리구현
class BinaryTree():
    def __init__(self):
        self.root = None
        self.nodes = {}

    # data, left, right를 인자로 받아서 각각의 노드를 생성
    # left, right는 생략가능하며 기본값은 None
    # 생성한 노드를 서로 연결
    # 모든 노드는 self.nodes에 딕셔너리형태로 저장됨.
    def node_connecting(self, data, left=None, right=None):
        if data not in self.nodes:
            self.nodes[data] = Node(data)
        if left != None:
            if left not in self.nodes:
                self.nodes[left] = Node(left)
                self.nodes[data].left = self.nodes[left]
            else:
                self.nodes[data].left = self.nodes[left]
        if right != None:
            if right not in self.nodes:
                self.nodes[right] = Node(right)
                self.nodes[data].right = self.nodes[right]
            else:
                self.nodes[data].right = self.nodes[right]

    # 전위 순회. 순서가 list로 반환됨.
    def preorder(self, node, trab=[]):
        trab.append(node.data)
        if node.left != None:
            self.preorder(node.left, trab)
        if node.right != None:
            self.preorder(node.right, trab)
        return trab

    # 후위 순회. 순서가 list로 반환됨.
    def postorder(self, node, trab=[]):
        if node.left != None:
            self.postorder(node.left, trab)
        if node.right != None:
            self.postorder(node.right, trab)
        trab.append(node.data)
        return trab

    # 중위 순회. 순서가 list로 반환됨.
    def inorder(self, node, trab=[]):
        if node.left != None:
            self.inorder(node.left, trab)
        trab.append(node.data)
        if node.right != None:
            self.inorder(node.right, trab)
        return trab
