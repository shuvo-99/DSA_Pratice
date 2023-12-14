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


  # ==============
  #  In this method we changed the node memory
  #  location instead of only swaping the data 
  #  amoung nodes
  # ==============

  def zigZag(self):
    tail = self.head
    count = 1
    if tail.next:
      if tail.next.next:
        if tail.data > tail.next.data:
          self.head = tail.next
          tail.next = tail.next.next
          self.head.next = tail
      
      else:
        if tail.data > tail.next.data:
            self.head = tail.next
            tail.next = None
            self.head.next = tail
    

    tail = self.head
    while tail.next:
      if tail.next.next: 
        if tail.next.next.next:
          if count%2 == 0:
            if tail.next.data > tail.next.next.data:
              temp = tail.next.next
              tail.next.next = temp.next
              temp.next = tail.next
              tail.next = temp
          
          else:
            if tail.next.data < tail.next.next.data:
              temp = tail.next.next
              tail.next.next = temp.next
              temp.next = tail.next
              tail.next = temp
        
        else:
          if count%2 == 0:
            if tail.next.data > tail.next.next.data:
              temp = tail.next.next
              tail.next.next = temp.next
              temp.next = tail.next
              tail.next = temp
          
          else:
            if tail.next.data < tail.next.next.data:
              temp = tail.next.next
              tail.next.next = temp.next
              temp.next = tail.next
              tail.next = temp

      count+=1
      tail = tail.next

# ll1 = LinekedList([4,3,7,8,6,2,1])
# ll1 = LinekedList([1,2,3,4])
# ll1 = LinekedList([11,15,20,5,10])
ll1 = LinekedList([61, 88, 41, 52, 14, 59, 44, 84, 34, 76, 94, 21])
ll1.printDetails()
ll1.zigZag()
ll1.printDetails()