# ------------------------------------------
# Solving using Tortoise and Hare algorithm
# ------------------------------------------


class Solution:
  def hasCycle(self, head):
    fast = head
    while fast and fast.next:
      head = head.next           # Go 1 step forward
      fast = fast.next.next      # Go 2 step forward

      if head is fast:
        return True
      
    return False

obj = Solution()
obj.hasCycle(head)               # As input, head of a circular linekd list will be given