class Node:
  def __init__(self,data):
    self.data = data
    self.prev_ref = None
    self.next_ref = None

class doublyLinkedList:
  def __init__(self):
    self.head = None

  # Forward traversal
  def printDteails(self):
    n = self.head

    if n == None:
      print('Doubly LL is empty')

    else:
      while n is not None:
        print(n.data,'-->',end=' ')
        n = n.next_ref
      print()
  
  # Backward traversal
  def printDteails_reverse(self):
    n = self.head

    if n == None:
      print('Doubly LL is empty')

    else:

      while n.next_ref is not None:       # Goto last node
        n = n.next_ref

      while n is not None:
        print(n.data,'-->',end=' ')
        n = n.prev_ref
      print()

  # Insert the 1st node
  def add1stNode(self, data):
    if self.head == None:
      new_node = Node(data)
      self.head = new_node

    else:
      print('Doubly LL is empty')
  
  # Insert at the begining
  def addBegin(self, data):
    new_node = Node(data)

    if self.head == None:                 # Check LL is empty or not
      self.head = new_node

    else:
      new_node.next_ref = self.head
      self.head.prev_ref = new_node
      self.head = new_node

  # Insert at the end
  def addEnd(self,data):
    new_node = Node(data)

    if self.head == None:                 # Check LL is empty or not
      self.head = new_node

    else:
      n =self.head
      while n.next_ref != None:    # Goto last node
        n = n.next_ref
      
      n.next_ref = new_node
      new_node.prev_ref = n

  # Insert a node after a given node
  def addInbetween_After(self, data, x):
    if self.head == None:
      print('Doubly LL is empty')
    
    else:
      
      n = self.head
      while n is not None:                  # Goto given node
        if x == n.data:
          break
        n = n.next_ref
      
      if n == None:
        print('Node not present')
      
      else:
        new_node = Node(data)
        new_node.next_ref = n.next_ref
        new_node.prev_ref = n

        if n.next_ref != None:               # if given node is not the last node
          n.next_ref.prev_ref = new_node
        
        n.next_ref = new_node
  
  # Insert a node before a given node
  def addInbetween_Before(self, data, x):
    if self.head == None:
      print('Doubly LL is empty')
    
    else:
      
      n = self.head
      while n is not None:                  # Goto given node
        if x == n.data:
          break
        n = n.next_ref
      
      if n == None:
        print('Node not present')
      
      else:
        new_node = Node(data)
        new_node.next_ref = n
        new_node.prev_ref = n.prev_ref

        if n.prev_ref != None:               # if given node is not the first node
          n.prev_ref.next_ref = new_node
        else:
          self.head = None
        
        n.prev_ref = new_node

  def delete_1stNode(self):
    if self.head == None:                            # Check Dll is empty or not
      print('Doubly LL is empty')
      return
    
    elif self.head.next_ref == None:                 # Check Dll has only one node or not
      self.head = None
      print('DLL is empty after deleteing 1st nide')
    
    else:
      self.head = self.head.next_ref
      self.head.prev_ref = None
  
  def delete_EndNode(self):
    if self.head == None:                            # Check Dll is empty or not
      print('Doubly LL is empty')
      return
    
    elif self.head.next_ref == None:                 # Check Dll has only one node or not
      self.head = None
      print('DLL is empty after deleteing 1st node')
    
    else:
      n = self.head
      while n.next_ref != None:
        n = n.next_ref
      n.prev_ref.next_ref = None

  def delete_byValue(self, x):
    if self.head == None:                            # Check Dll is empty or not
      print('Doubly LL is empty')
      return
    
    elif self.head.next_ref == None:                 # Check if Dll has only one node 
      if x == self.head.data:                        # Check if it is the deleted node
        self.head = None
      else:
        print('Node not present')
      return
    
    elif x == self.head.data:                        # Check if it is the 1st node
        self.head = self.head.next_ref
        self.head.prev_ref = None
        return
    
    else:

      n = self.head
      while n.next_ref != None:                      # Iterate for looking the middle node
        if x == n.data:
          break
        n = n.next_ref
      
      if n.next_ref != None:                         # Check if it is middle node
        n.next_ref.prev_ref = n.prev_ref 
        n.prev_ref.next_ref = n.next_ref

      else:                                          # If it is last node
        if x == n.data:
          n.prev_ref.next_ref = None
        else:
          print('Node not present')



    


    






dll1 = doublyLinkedList()
dll1.add1stNode(20)
dll1.printDteails()
dll1.addBegin(10)
dll1.printDteails()
dll1.addBegin(5)
dll1.printDteails()
dll1.addEnd(100)
dll1.printDteails()
dll1.addEnd(200)
dll1.printDteails()
dll1.addInbetween_After(30,20)
dll1.printDteails()
dll1.addInbetween_Before(40,100)
dll1.printDteails()
dll1.printDteails_reverse()
dll1.delete_1stNode()
dll1.printDteails()
dll1.delete_EndNode()
dll1.printDteails()
dll1.delete_byValue(100)
dll1.printDteails()
dll1.delete_byValue(30)
dll1.printDteails()
dll1.delete_byValue(10)
dll1.printDteails()
    