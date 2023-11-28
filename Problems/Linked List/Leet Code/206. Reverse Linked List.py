# ------------------------------------------
# Solving using three pointers curr, prev, and next 
# ------------------------------------------


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self, lst):
    self.head = None

    for i in lst:
      self.insert(i)

  def insert(self, data):
    new_node = Node(data)
    
    if self.head == None:
      self.head = new_node
    
    elif self.head.next == None:
      self.head.next = new_node

    else:

      tail = self.head
      while tail.next != None:
        tail = tail.next
      tail.next = new_node

  def printDeatils(self):
    tail = self.head
    while tail!= None:
      print(tail.val,'-->',end=' ')
      tail = tail.next
    print()

class Solution:
  def reverseList(self, head):
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    
    return head
  
  def printDeatils2(self, head):
    tail = head
    while tail!= None:
      print(tail.val,'-->',end=' ')
      tail = tail.next
    print() 



ll1 = LinkedList([1,2,3,4,5])
ll1.printDeatils()
obj = Solution()
m = obj.reverseList(ll1.head)  
obj.printDeatils2(m)