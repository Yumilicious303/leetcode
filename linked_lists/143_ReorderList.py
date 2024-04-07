#Reorder List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        slow = temp
        
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        curr1 = head
        curr2 = prev

        dummy = ListNode()
        currentmerged = dummy

        while curr1 and curr2:
            currentmerged.next = curr1
            curr1 = curr1.next
            currentmerged = currentmerged.next

            currentmerged.next = curr2
            curr2 = curr2.next
            currentmerged = currentmerged.next
        
        if curr1:
            currentmerged.next = curr1
        if curr2:
            currentmerged.next = curr2
        
        dummy.next = None
        
class SolutionNeet:
    def reorderList(self, head):
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        #merge two halves
        first, second = head, prev
        while second:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first, second = next1, next2




node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

sol = Solution()
sol.reorderList(node1)