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

  def delete(self, data, curr):
    if self.key == None:
      print('Tree is empty')

    else:
      if data < self.key:
        if self.left_child:
          self.left_child = self.left_child.delete(data, curr)
        else:
          print(' Node not present')
      
      elif data > self.key:
        if self.right_child:
          self.right_child = self.right_child.delete(data, curr)
        else:
          print(' Node not present')

      else:
        if self.left_child == None:             # If Deleted Node has 0 or 1 child
          temp = self.right_child               #
          if data == curr:                      # If deleted node is the root node
            self.key = temp.key
            self.left_child = temp.left_child
            self.right_child = temp.right_child
            temp = None
            return
          self = None                           #
          return temp                           #
        
        if self.right_child == None:            # If Deleted Node has 0 or 1 child
          temp = self.left_child                #
          if data == curr:                      # If deleted node is the root node
            self.key = temp.key
            self.left_child = temp.left_child
            self.right_child = temp.right_child
            temp = None
            return
          self = None                           #  
          return temp                           #
        
        node = self.right_child                 # If Deleted Node has 2 child
        while node.left_child:
          node = node.left_child
        self.key = node.key
        self.right_child = self.right_child.delete(node.key, curr)
      return self
        
  def min_node(self):
    current = self
    while current.left_child != None:
      current = current.left_child
    print("Node with smallest key is =", current.key)
  
  def max_node(self):
    current = self
    while current.right_child != None:
      current = current.right_child
    print("Node with smallest key is =", current.key)
    
def count(node):                                              # Find the no. of nodes in the tree
  if node == None:
    return 0
  return 1 + count(node.left_child) + count(node.right_child)


# --------------------------
root = BST(10)

# lst = [6,3,1,6,98,3,7]
lst = [1, 12]

for i in lst:
  root.insertInBST(i)

print('No. of nodes in the tree =',count(root))

root.search(30)

print('===== Pre-Order ====')
root.pre_order()
print()

print('===== In-Order ====')
root.in_order()
print()

print('===== Post-Order ====')
root.post_order()
print()

root.min_node()
root.max_node()

if count(root) > 1:
  root.delete(10, root.key)
else:
  print("Can't perform delete operation beacuse it's a root node")

print('===== Pre-Order ====')
root.pre_order()
print()