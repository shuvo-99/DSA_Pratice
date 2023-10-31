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

class Solution:
  
  def deleteDuplicates(self, head):
    if head != None:
      n = head
      tail = head.next
      while tail != None:
        if tail.data == n.data:
          n.next = tail.next
          tail = tail.next

        else:
          tail = tail.next
          n = n.next
    return head
  
  def printDetails2(self,head):
      if head ==None:
        print('LL is empty')
      
      else:
        n = head
        while n != None:
          print(n.data,'-->', end=' ')
          n = n.next
        print()    

ll1 = LinkedList([])
# ll1 = LinkedList([1,1,2,2,3,3,3])
ll1.printDetails()

obj = Solution()
new_head = obj.deleteDuplicates(ll1.head)
obj.printDetails2(new_head)