class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class linkedList:
  def __init__(self, lst):
    self.head = None

    for i in lst:
      self.insert(i)

  def insert(self, val):
    new_node = Node(val)

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
  def removeElements(self, head, val):
    
    if head == None:
      return head
    
    else:

      self.head = head
      tail = self.head
      while tail!= None:
        if self.head.val == val:
          self.head = self.head.next
          tail = self.head
          continue

        
        
        elif tail.val == val:
          tail = self.head
          continue
        elif tail.next.val == val:
          tail.next = tail.next.next
        
        elif tail.next == None:
          return self.head
        
        tail = tail.next

      
      return self.head
    
  # Alternative Efficient approach
  
  # def removeElements(self, head, val):
    # Create a dummy node to serve as the new head, which makes it easier to handle edge cases.
    # dummy = Node(0)
    # dummy.next = head
    # current = dummy

    # while current.next:
    #     if current.next.val == val:
    #         current.next = current.next.next
    #     else:
    #         current = current.next

    # return dummy.next
    

  def printDeatils2(self, head):
    tail = head
    while tail!= None:
      print(tail.val,'-->',end=' ')
      tail = tail.next
    print()  
  


ll1 = linkedList([1,2,6,3,4,5,6])
# ll1 = linkedList([])
# ll1 = linkedList([7,7,7,7])
# ll1 = linkedList([1])
# ll1 = linkedList([1,2,2,1])
# ll1 = linkedList([5,4,3,2,1,1])
ll1.printDeatils()
obj = Solution()
m = obj.removeElements(ll1.head, 6)
# m = obj.removeElements(ll1.head, 1)
# m = obj.removeElements(ll1.head, 7)
# m = obj.removeElements(ll1.head, 2)
# m = obj.removeElements(ll1.head, 2)
# m = obj.removeElements(ll1.head, 1)
obj.printDeatils2(m)



