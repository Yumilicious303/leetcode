class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def createLinkedList(self, val_array):
        current = None
        for value in val_array:
            new_node = ListNode(value)
            if self.head is None:
                self.head = new_node
            if current is not None:
                current.next = new_node
                current = current.next
            else:
                current = new_node

    def printLL(self):
        current = self.head
        while current is not None:
            if current.next is not None:
                print(f'Value: {current.val}, Next: {current.next.val}')
            else:
                print(f'Value: {current.val}, Next: None')
            current = current.next

