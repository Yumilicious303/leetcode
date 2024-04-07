#Merge K Sorted Lists
import heapq
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)


node1_5 = ListNode(5)
node1_4 = ListNode(4, node1_5)
node1_1 = ListNode(1, node1_4)

node2_4 = ListNode(4)
node2_3 = ListNode(3, node2_4)
node2_1 = ListNode(1, node2_3)

node3_6 = ListNode(6)
node3_2 = ListNode(2, node3_6)


lists = [node1_1, node2_1, node3_2]

def mergeKLists(lists):
    head = ListNode(0)
    current = head
    heap = []
    for i in range(len(lists)):
        if lists[i] is not None:
            heap.append([lists[i].val, i, lists[i]])
    heapq.heapify(heap)

    while heap:
        popped = heapq.heappop(heap)
        node = popped[2]
        current.next = node
        if node.next is not None:
            i += 1
            heapq.heappush(heap, [node.next.val, i, node.next])
        current = node
    
    return head.next


#mergeKLists(lists)



class SolutionNeet:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
    
sol = SolutionNeet()
print(sol.mergeKLists(lists))