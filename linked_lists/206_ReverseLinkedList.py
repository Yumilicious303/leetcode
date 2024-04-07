#Reverse Linked List
from basicLinkedList import *

def reverseList(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev





myList = LinkedList()
myList.createLinkedList([1,2,3,4,5])
rev = reverseList(myList.head)

