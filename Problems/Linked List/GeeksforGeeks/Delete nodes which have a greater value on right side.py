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

  # Process - 1: 
  def removeNode(self):
    
    # Start from the head node
    currentNode = self.head
    prevNode = None

    while currentNode:
      # Get the value of the current node
      value = currentNode.data
      # Variable to track if a greater value is found
      found = False
      # Runner node to search for greater values
      runner = currentNode.next

      while runner:
          # If a greater value is found, update the found flag and break the loop
          if runner.data > value:
              found = True
              break
          runner = runner.next

      if found:
          # If a greater value is found, update the current node's value and next pointer
          if prevNode:
              prevNode.next = runner
          else:
              # If the current node is the head, update the head to the next node
              self.head = runner
          currentNode = runner
      else:
          # If no greater value is found, move to the next node
          prevNode = currentNode
          currentNode = currentNode.next


ll1 = LinekedList([12,15,10,11,6,12,3])
ll1.printDetails()
ll1.removeNode()
ll1.printDetails()