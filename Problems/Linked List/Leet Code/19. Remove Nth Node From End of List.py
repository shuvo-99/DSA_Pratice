class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

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

  def printDetails(self, head):
    tail = head
    while tail:
      print(tail.val,'-->',end=' ')
      tail = tail.next
    print()

  def removeNthFromEnd(self, head,n):

    # ---------------- PROCESS - 1 -----------------
    # dummy = Node(0, head)
    # left = dummy
    # right = head

    # while n>0:
    #   right = right.next
    #   n-=1

    # while right:
    #   left = left.next
    #   right = right.next

    # left.next = left.next.next

    # return dummy.next

    # ---------------- PROCESS - 2 ------------------
    left = head
    right = head

    while n>0:
        right = right.next
        n-=1

    if not right:
        return head.next

    while right.next:
        left = left.next
        right = right.next

    left.next = left.next.next

    return head




# ll1 = LinekedList([1,2,3,4,5])
ll1 = LinekedList([1])
ll1.printDetails(ll1.head)
h = ll1.removeNthFromEnd(ll1.head,1)
ll1.printDetails(h)