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

  def search(self, data):
    if self.key == data:
      print('node found')
      
    elif data < self.key:
      if self.left_child:
        self.left_child.search(data)
      else:
        print('Node not found')

    else:
      if self.right_child:
        self.right_child.search(data)
      else:
        print('Node not found')    
    
  def pre_order(self):
    print(self.key,'-->',end=' ')
    if self.left_child:
      self.left_child.pre_order()
    if self.right_child:
      self.right_child.pre_order()
    

  def in_order(self):
    if self.left_child:
      self.left_child.in_order()
    print(self.key,'-->',end=' ')
    if self.right_child:
      self.right_child.in_order()
  
  def post_order(self):
    if self.left_child:
      self.left_child.post_order()
    if self.right_child:
      self.right_child.post_order()
    print(self.key,'-->',end=' ')

root = BST(10)
lst = [5,15,4,20,3,21]
for i in lst:
  root.insertInBST(i)
print(root.key)
print(root.left_child)
print(root.right_child)
root.search(30)
print('===== Pre-Order ====')
root.pre_order()
print()
print('===== In-Order ====')
root.in_order()
print()
print('===== Post-Order ====')
root.post_order()