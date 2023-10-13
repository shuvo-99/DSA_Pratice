class Node:
  def __init__(self,data):
    self.data = data
    self.prev_ref = None
    self.next_ref = None

class doublyLinkedList:
  def __init__(self):
    self.head = None

  # Forward traversal
  def printDteails(self):
    n = self.head

    if n == None:
      print('Doubly LL is empty')

    else:
      while n is not None:
        print(n.data,'-->',end=' ')
        n = n.next_ref
  
  # Backward traversal
  def printDteails_reverse(self):
    n = self.head

    if n == None:
      print('Doubly LL is empty')

    else:

      while n.nref is not None:       # Goto last node
        n = n.next_ref

      while n is not None:
        print(n.data,'-->',end=' ')
        n = n.prev_ref

  # Insert the 1st node
  def add1stNode(self, data):
    if self.head == None:
      new_node = Node(data)
      self.head = new_node

    else:
      print('Doubly LL is empty')


ll1 = doublyLinkedList()


    

    