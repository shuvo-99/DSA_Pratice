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
      print()
  
  # Backward traversal
  def printDteails_reverse(self):
    n = self.head

    if n == None:
      print('Doubly LL is empty')

    else:

      while n.next_ref is not None:       # Goto last node
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
  
  # Insert at the begining
  def addBegin(self, data):
    new_node = Node(data)

    if self.head == None:                 # Check LL is empty or not
      self.head = new_node

    else:
      new_node.next_ref = self.head
      self.head.prev_ref = new_node
      self.head = new_node

  # Insert at the end
  def addEnd(self,data):
    new_node = Node(data)

    if self.head == None:                 # Check LL is empty or not
      self.head = new_node

    else:
      n =self.head
      while n.next_ref != None:    # Goto last node
        n = n.next_ref
      
      n.next_ref = new_node
      new_node.prev_ref = n


dll1 = doublyLinkedList()
dll1.add1stNode(20)
dll1.printDteails()
dll1.addBegin(10)
dll1.printDteails()
dll1.addBegin(5)
dll1.printDteails()
dll1.addEnd(100)
dll1.printDteails()
dll1.addEnd(200)
dll1.printDteails()
dll1.printDteails_reverse()
    

    