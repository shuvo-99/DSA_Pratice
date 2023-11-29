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

def multiply(head1, head2):
  tail1 = head1
  tail2 = head2

  num1 = 0
  num2 = 0

  while tail1 or tail2:
    if tail1:
      num1 = num1*10 + tail1.data
      tail1 = tail1.next
    
    if tail1:
      num2 = num2*10 + tail2.data
      tail2 = tail2.next

  res = num1 * num2
  print(res)

ll1 = LinekedList([9,4,6])
ll1.printDetails()
ll2 = LinekedList([8,4])
ll2.printDetails()
multiply(ll1.head, ll2.head)