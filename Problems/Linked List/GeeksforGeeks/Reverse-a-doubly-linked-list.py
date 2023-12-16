class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class LinekedList:
  def __init__(self, lst):
    self.head = None

    for i in lst:
      self.forwardinsert(i)

    self.backwardinsert()
  
  def forwardinsert(self, val):
      
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

  def backwardinsert(self):
    n = self.head
    while n.next:
      n.next.prev = n
      n = n.next
  
  def forwardprintDetails(self):
    tail = self.head
    while tail:
      print(tail.data,'-->',end=' ')
      tail = tail.next
    print()
  
  def backwardprintDetails(self):
    tail = self.head
    while tail.next:
      tail = tail.next

    while tail:
      print(tail.data,'-->',end=' ')
      tail = tail.prev
    print()

  def reverseDLL(self):
    n  = self.head
    while n.next:
      n = n.next
    
    while n:
      if n.next == None:
          self.head = n
          n.next = n.prev
          n.prev = None
          
      else:
          temp = n.next
          n.next = n.prev
          n.prev = temp
      n = n.next
    # return head
        
ll1 = LinekedList([12,15,10,11,6,12,3])
ll1.forwardprintDetails()
ll1.backwardprintDetails()
ll1.reverseDLL()
ll1.forwardprintDetails()
ll1.backwardprintDetails()