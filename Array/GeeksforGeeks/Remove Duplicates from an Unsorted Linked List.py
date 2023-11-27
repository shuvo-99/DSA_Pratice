class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinekedList:
  def __init__(self, lst):
    self.head = None

    for i in lst:
      self.insert(i)

  def insert(self, val):
      
    new_Node = Node(val)
      
    if self.head == None:
      self.head = new_Node

    elif self.head.next == None:
      self.head.next = new_Node
      
    else:
      tail = self.head  
      while tail.next != None:
        tail = tail.next
      tail.next = new_Node

  def printDetails(self):
    tail = self.head
    while tail:
      print(tail.data,'-->',end=' ')
      tail = tail.next
    print()

  def removeDuplicate(self):
    pointer1 = self.head
    pointer2 = None

    while pointer1:
      pointer2 = pointer1

      while pointer2.next:
        if pointer1.data == pointer2.next.data:
          pointer2.next = pointer2.next.next
          
        else:
          pointer2 = pointer2.next
      
      pointer1 = pointer1.next


ll1 = LinekedList([12,11,12,21,41,43,21])
ll1.printDetails()
ll1.removeDuplicate()
ll1.printDetails()