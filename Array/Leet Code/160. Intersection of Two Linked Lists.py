class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, lst):
    self.head = None

    if len(lst) != 0:
      for i in lst:
        self.insert(i)
  
  def insert(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node

    else:

      if self.head.next == None:
        self.head.next = new_node
      
      else:
        tail = self.head
        
        while tail.next != None:
          tail = tail.next
        tail.next = new_node  

  def printDetails(self):
    if self.head ==None:
      print('LL is empty')
    
    else:
      n = self.head
      while n != None:
        print(n.data,'-->', end=' ')
        n = n.next
      print()

  def merge(self, head):
    n = self.head

    while n.next != None:
      n = n.next
    n.next = head

class Solution:
  def getIntersectionNode(self, headA, headB):
    
    a = headA
    b = headB

    while a != b:
      if a:
        a = a.next
      else: 
        a = headB
      if b:
        b = b.next
      else:
        b = headA

    print(a.data)
    return a

ll1 = LinkedList([4,1])
ll1.printDetails()
ll2 = LinkedList([5,6,1])
ll2.printDetails()
ll3 = LinkedList([8,4,5])
ll3.printDetails()
ll1.merge(ll3.head)
ll1.printDetails()
ll2.merge(ll3.head)
ll2.printDetails()

obj = Solution()
obj.getIntersectionNode(ll1.head, ll2.head)