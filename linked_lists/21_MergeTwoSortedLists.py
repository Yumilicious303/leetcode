#Merge Two Sorted Lists
from basicLinkedList import *

def mergeTwoLists(list1head, list2head):
    initial = ListNode()
    currentMerged = initial
    current1 = list1head
    current2 = list2head

    while current1 and current2:
        if current1.val <= current2.val:
            currentMerged.next = current1
            current1 = current1.next
        else:
            currentMerged.next = current2
            current2 = current2.next
        currentMerged = currentMerged.next
    if current1:
        currentMerged.next = current1
    if current2:
        currentMerged.next = current2
    return initial.next


list1 = LinkedList()
list2 = LinkedList()
list1.createLinkedList([1,2,4])
list2.createLinkedList([1,3,4])

mergeTwoLists(list1.head, list2.head)

