class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.child = None

class LinkedList:
  def __init__(self, lst):
    self.head = None
    for i in lst:
      self.insert(i)

  def insert(self, elem):
    new_Node = Node(elem)
    if self.head == None:
      self.head = new_Node

    elif self.head.next == None:
      self.head.next = new_Node

    else:
      tail = self.head
      while tail.next:
        tail = tail.next
      tail.next = new_Node

  def printDetails(self):
    tail = self.head
    while tail:
        print(tail.data,'-->',end=' ')
        tail = tail.next
    print()

def flatten(head):
  tail = current = head
  while tail.next:
    tail = tail.next
  
  while current != tail:
    if current.child:
      tail.next = current.child

      while tail.next:
        tail = tail.next
    current = current.next

  printList(head)

def printList(head):  
    if not head:  
        return
    print('After Flatteing')
    while(head):  
      
      print(head.data,'-->',end = " ")  
      head = head.next
    print()
      

ll1 = LinkedList([10,5,12,7,11])
ll1.printDetails()
ll2 = LinkedList([4,20,13])
ll2.printDetails()
ll3 = LinkedList([17,6])
ll3.printDetails()
ll4 = LinkedList([9,18])
ll4.printDetails()
ll5 = LinkedList([19,15])
ll5.printDetails()

ll1.head.child = ll2.head                # 10 -> 4
ll1.head.next.next.next.child = ll3.head # 7 -> 17
ll2.head.next.child = Node(2)            # 20 -> 2
ll2.head.next.next.child = Node(16)      # 13 -> 16
ll2.head.next.next.child.child = Node(3) # 16 -> 3
ll3.head.child = ll4.head
ll4.head.child = ll5.head

flatten(ll1.head)



