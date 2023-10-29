class BST:
  def __init__(self, key):
    self.key = key
    self.left_child = None
    self.right_child = None

  def insertInBST(self, data):
    if self.key == None:
      self.key == data
      return
    
    elif self.key == data:
      print('Duplicate value are not added')
      return

    else:
      if self.key > data:
        if self.left_child == None:
          self.left_child = BST(data)

        else:
          self.left_child.insertInBST(data)

      else:
        if self.right_child == None:
          self.right_child = BST(data)

        else:
          self.right_child.insertInBST(data)

    

root = BST(10)
root.insertInBST(20)
print(root.key)
print(root.left_child)
print(root.right_child)