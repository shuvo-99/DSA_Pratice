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

def MergeNode(head1,head2):
    head2.next.next.next = head1.next.next.next
 
# Function to find the intersection of two node
def FindMegeNode(n1, n2):
     
    # Define hashset
    hs = set()
 
    while (n1 != None):
        hs.add(n1)
        n1 = n1.next
    while (n2 != None):
        if (n2 in hs):
            return n2.data
        n2 = n2.next
     
    return None
 
 
# Driver code
ll1 = LinekedList([1,2,3,4,5,6,7])
ll2 = LinekedList([10,9,8])

MergeNode(ll1.head, ll2.head)

ll1.printDetails()
ll2.printDetails()
 
print(FindMegeNode(ll1.head, ll2.head))