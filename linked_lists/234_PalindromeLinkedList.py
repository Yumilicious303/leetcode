#Palindrome Linked List
from basicLinkedList import *


def isPalindrome(head):
    #find middle of linked List
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    #reverse second half of linkedlist
    prev = None
    while slow:
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next

    #iterate over the linkedlist from both ends and compare
    l, r = head, prev
    while l and r:
        if l is None or r is None:
            return False
        if l.val != r.val:
            return False
        l = l.next
        r = r.next
    return True

        

myList = LinkedList()
myList.createLinkedList([1,2,2,1])
print(isPalindrome(myList.head))