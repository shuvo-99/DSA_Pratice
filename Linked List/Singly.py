class Node:
  def __init__(self, data):
    self.data = data
    self.ref = None

class LinkedList:
  def __init__(self):
    self.head = None

  # traverse
  def printDteails(self):
    n = self.head
    
    if n is None:
      print('Linked List is Empty')

    else:
      while n != None:
        print(n.data)
        n = n.ref

  # add at the begining
  def addBegin(self,data):
    new_node = Node(data)
    new_node.ref = self.head
    self.head = new_node

  # add at the end
  def addEnd(self, data):
    new_node = Node(data)

    # check Linked List empty or not
    if self.head == None:
      self.head = new_node

    else:
      n = self.head
      while n.ref != None:
        n = n.ref
      n.ref = new_node


ll1 = LinkedList()
ll1.addBegin(10)
ll1.addEnd(100)
ll1.addBegin(20)
ll1.printDteails()