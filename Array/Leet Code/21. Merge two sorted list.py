class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
  def __init__(self, l):
    self.head = None

    for i in l:
      self.insert(i)

  def printDetails(self):
    if self.head ==None:
      print('LL is empty')
    
    else:
      n = self.head
      while n != None:
        print(n.val,'-->', end=' ')
        n = n.next
      print()

  def insert(self,data):
    if self.head == None:
      new_node = ListNode(data)
      self.head = new_node
    
    else:
      if self.head.next == None:
        new_node = ListNode(data)
        self.head.next = new_node
      else:
        n = self.head
        while n.next != None:
          n = n.next
        new_node = ListNode(data)
        n.next = new_node



class Solution:
    def mergeTwoLists(self, list1, list2):
      dummy = ListNode(0)
      current = dummy

      while list1 is not None and list2 is not None:
          if list1.val < list2.val:
              current.next = list1
              list1 = list1.next
          else:
              current.next = list2
              list2 = list2.next
          current = current.next

      if list1 is not None:
          current.next = list1
      else:
          current.next = list2
      
      # self.head = dummy.next
      return dummy.next
    
    def printDetails2(self,head):
      if head ==None:
        print('LL is empty')
      
      else:
        n = head
        while n != None:
          print(n.val,'-->', end=' ')
          n = n.next
        print()


ll1 = LinkedList([1,2,4])
# ll1.printDetails()
# ll1.insert(1)
# ll1.printDetails()
# ll1.insert(2)
# ll1.printDetails()
# ll1.insert(4)
ll1.printDetails()

ll2 = LinkedList([1,3,4])
ll2.printDetails()

obj = Solution()
merged_head = obj.mergeTwoLists(ll1.head, ll2.head)

print("Merged Linked List:")
obj.printDetails2(merged_head)



