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

  def segregate(self):

  # === Process - 1 ===
    
  #   dummy = Node(0)
  #   tail = self.head
  #   d_tail = dummy

  #   while tail.next:
  #     if tail.next.next:
  #       if tail.next.data%2 == 0:
  #         while d_tail.next:
  #           d_tail = d_tail.next
  #         d_tail.next = tail.next
  #         tail.next = tail.next.next
  #         d_tail.next.next = None 
  #         tail = tail
  #       else:  
  #         tail = tail.next
      
  #     else:
  #       if tail.next.data%2 == 0:
  #         while d_tail.next:
  #           d_tail = d_tail.next
  #         d_tail.next = tail.next
  #         tail.next = None
  #         tail = tail
  #       else:  
  #         tail = tail.next

    
  #   while d_tail.next:
  #     d_tail = d_tail.next
  #   d_tail.next = self.head
  #   self.head = dummy.next
    
  #  === Process -2 ===
  
    dummy_even = Node(0)
    dummy_odd = Node(0)

    tail = self.head
    even_tail = dummy_even
    odd_tail = dummy_odd

    while tail:
        if tail.data % 2 == 0:
            even_tail.next = tail
            even_tail = even_tail.next
        else:
            odd_tail.next = tail
            odd_tail = odd_tail.next
        tail = tail.next

    even_tail.next = dummy_odd.next
    odd_tail.next = None

    self.head = dummy_even.next


ll1 = LinekedList([17, 15,8,12,10, 5,4,1,7,6])
# ll1 = LinekedList([17,8])
ll1.printDetails()
ll1.segregate()
ll1.printDetails()