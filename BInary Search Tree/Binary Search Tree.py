class BST:
  def __init__(self, key):
    self.key = key
    self.left_child = None
    self.right_child = None

root = BST(10)
print(root.key)
print(root.left_child)
print(root.right_child)