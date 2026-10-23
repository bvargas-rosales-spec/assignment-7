class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    pass 
    def __init__(self, root=None): 
        self.root = root
    
    def insert(self, parent_name, child_name, side):
        new_node = DoctorNode(child_name)

        if self.root is None:
            self.root = new_node
            return True
        
        parent = self._find(self.root, parent_name)
        if parent is None:
            print(f"Parent '{parent_name}' not found.")
            return False
        
        if side == "left":
            if parent.left is not None:
                print(f"{parent_name} already has a left report.")
                return False
            parent.left = new_node
        elif side == "right":
            if parent.right is not None: 
                print(f"{parent_name} already has a right report.")
                return False
            parent.right = new_node
        else: 
            print("Side must be left or right.")
            return False
        
        return True
    
    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name: 
            return node
        
        found = self._find(node.left, name)
        if found is not None:
            return found
        return self._find(node.right, name)

    def preorder(self,node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)
    
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)
    
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here

tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print("Preorder: ", tree.preorder(tree.root))
print("Inorder:  ", tree.inorder(tree.root))
print("Postorder:", tree.postorder(tree.root))

assert tree.preorder(tree.root) == ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
assert tree.inorder(tree.root) == ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
assert tree.postorder(tree.root) == ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]

before = tree.preorder(tree.root)
assert tree.insert("Dr. Nobody", "Dr. Ghost", "left") == False
assert tree.preorder(tree.root) == before

assert tree.insert("Dr. Goldsmith", "Dr. Wong", "middle") == False
assert tree.insert("Dr. Goldsmith", "Dr. Wong", None) == False
assert tree.preorder(tree.root) == before

assert tree.insert("Dr. Croft", "Dr. Chen", "left") == False
assert tree.root.left.name == "Dr. Phan"

empty = DoctorTree()
assert empty.preorder(empty.root) == []

print("All tests passed!")