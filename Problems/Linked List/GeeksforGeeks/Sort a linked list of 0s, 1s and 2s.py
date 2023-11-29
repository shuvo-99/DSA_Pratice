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

  def sortLL(self):
    countlist = [0,0,0]
    tail = self.head

    while tail:
      countlist[tail.data] += 1
      tail = tail.next
    # print(countlist)
    n = 0
    tail = self.head
    while tail:
      if countlist[n] == 0:
        n += 1
      else:
        countlist[n] -= 1
        tail.data = n
        tail = tail.next

ll1 = LinekedList([1,1,2,0,2,0,1])
ll1.printDetails()
ll1.sortLL()
ll1.printDetails()