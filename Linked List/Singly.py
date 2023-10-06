class Node:
  def __init__(self, data):
    self.data = data
    self.ref = None

class LinkedList:
  def __init__(self, node_ref=None):
    self.head = node_ref

  def printDteails(self):
    n = self.head
    
    if n is None:
      print('Linked List is Empty')

    else:
      while n.ref != None:
        print(n.data)
        n = n.ref

ll1 = LinkedList()
ll1.printDteails()