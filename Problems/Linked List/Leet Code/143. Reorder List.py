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

  def printDetails(self):
    tail = self.head
    while tail:
      print(tail.val,'-->',end=' ')
      tail = tail.next
    print()

  def reorderList(self, head):
    
    # # === find middle and final point ===
    # slow = fast = head

    # while fast and fast.next:
    #   fast = fast.next.next
    #   slow = slow.next
    
    # # === Detach into two linked list ===
    # temp_head = slow.next
    # slow.next = None

    # # ==== Reverse right side list ====
    # prev = None
    # current = temp_head
    # while(current is not None):
    #     next = current.next
    #     current.next = prev
    #     prev = current
    #     current = next
    # temp_head = prev

    # # === Merge two linked list on the the left liked list ===
    # node1, node2 = head, temp_head
    # while node1 and node2:
    #     nextNode1 = node1.next
    #     nextNode2 = node2.next

    #     node1.next = node2
    #     node1 = nextNode1

    #     node2.next = node1
    #     node2 = nextNode2

    # ===================================
    # ======== Better Approach ==========
    # ===================================

    # === find middle and final point ===
    slow,fast = head,head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    # === Detach into two linked list ===
    curr = slow.next
    prev=slow.next=None

    # ==== Reverse right side list ====
    while curr:
        nxt = curr.next
        curr.next = prev
        prev=curr
        curr=nxt
    first,second=head,prev

    # === Merge two linked list on the the left liked list ===
    while second:
        fnxt,snxt = first.next,second.next
        first.next = second
        second.next = fnxt
        first=fnxt
        second=snxt

  def printDetails2(self, head):
    tail = head
    while tail:
      print(tail.val,'-->',end=' ')
      tail = tail.next
    print()

ll1 = LinekedList([1,2,3,4,5])
ll1.printDetails()
ll1.reorderList(ll1.head)
# ll1.printDetails2(ll1.head)
ll1.printDetails()
