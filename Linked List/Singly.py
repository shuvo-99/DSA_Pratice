class Node:
  def __init__(self, data):
    self.data = data
    self.ref = None

class LinkedList:
  def __init__(self):
    self.head = None

  # traverse
  def printDteails(self):
    n = self.head
    
    if n is None:
      print('Linked List is Empty')

    else:
      while n != None:
        print(n.data)
        n = n.ref

  # add at the begining
  def addBegin(self,data):
    new_node = Node(data)
    new_node.ref = self.head
    self.head = new_node

  # add at the end
  def addEnd(self, data):
    new_node = Node(data)

    # check Linked List empty or not
    if self.head == None:
      self.head = new_node

    else:
      n = self.head
      while n.ref != None:
        n = n.ref
      n.ref = new_node

  # add inbetween node - after a node
  def addInbetween_After(self, data, x):
    n = self.head
    while n!= None:              #Check LL is empty or node is present or not
      if x == n.data:
        break
      n = n.ref
    
    if n == None:
      print('Node not present')

    else:
      new_node = Node(data)      #create new node  
      new_node.ref = n.ref       #set its ref to next node
      n.ref = new_node           #set its prev node ref to its node

  # add inbetween node - before a node
  def addInbetween_Before(self, data, x):
    if self.head == None:
      print('LL in empty')
      return
    
    # before 1st node
    if self.head.data == x:
      new_node = Node(data)       #create new node
      new_node.ref = self.head    #set its ref to next node
      self.head = new_node        #set its node as head
      return
    
    # before rest nodes
    n = self.head
    while n.ref != None:          #Check node is present or not
      if n.ref.data == x:         #if present break loop
        break
      n = n.ref

    if n.ref == None:
      print('Node not present')
    else:
      new_node = Node(data)      #create new node
      new_node.ref = n.ref       #set its ref to next node
      n.ref = new_node           #set its prev node ref to its node

  # add node when LL is empty
  def add_1st_node(self, data):
    if self.head == None:
      new_node = Node(data)
      self.head = new_node
    
    else:
      print('LL not empty')


ll1 = LinkedList()
ll1.add_1st_node(5)
ll1.addBegin(10)
ll1.addEnd(100)
ll1.addBegin(20)
ll1.addInbetween_After(30,10)
ll1.addInbetween_Before(25,20)
ll1.addInbetween_Before(40,100)
ll1.printDteails()