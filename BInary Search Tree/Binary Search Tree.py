class BST:
  def __init__(self, key):
    self.key = key
    self.left_child = None
    self.right_child = None

  def insertInBST(self, data):

    if self.key == None:                       # Check if tree is empty or not
      self.key == data                         # If empty, insert as first node
      return
    
    elif self.key == data:                     # Check the value is duplicate
      print('Duplicate value are not added')   # If duplicate, we ignore the value
      return

    else:                                      # Finding the position of the new_Node
      if self.key > data:                      # Check the value is greater or less than the root value
        if self.left_child == None:            # if less than root value, check root's left cild is empty or not
          self.left_child = BST(data)          # if empty, create a new node and store its address in the left child of the root

        else:
          self.left_child.insertInBST(data)    # if root's left cild is not empty, then repeat the process and now new root will be the previous root's left cild

      else:
        if self.right_child == None:           # if greater than root value, check root's right cild is empty or not 
          self.right_child = BST(data)         # if empty, create a new node and store its address in the right child of the root

        else:
          self.right_child.insertInBST(data)   # if root's right cild is not empty, then repeat the process and now new root will be the previous root's right cild

    

root = BST(10)
root.insertInBST(20)
print(root.key)
print(root.left_child)
print(root.right_child)