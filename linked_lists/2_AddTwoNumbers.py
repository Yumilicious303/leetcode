#Add Two Numbers
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2):
        l1_string = ''
        l2_string = ''

        c1 = l1
        c2 = l2

        while c1 is not None:
            l1_string += str(c1.val)
            c1 = c1.next

        while c2 is not None:
            l2_string += str(c2.val)
            c2 = c2.next
        
        l1_string = l1_string[::-1]
        l2_string = l2_string[::-1]

        result_int = int(l1_string) + int(l2_string)
        result_str = str(result_int)[::-1]

        dummy = ListNode()
        cur = dummy

        for c in result_str:
            node = ListNode(int(c))
            cur.next = node
            cur = cur.next
        
        return dummy.next

def addTwoNumbersNeet(l1, l2):
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        #new digit
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

def addTwoNumbers2(l1, l2):
    dummy = ListNode()
    cur = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        value = (carry + val1 + val2) % 10
        carry = (carry + val1 + val2) // 10
        node = ListNode(value)
        cur.next = node
        cur = cur.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next


node3 = ListNode(3)
node7 = ListNode(7, node3)
node0 = ListNode(0)

print(addTwoNumbers2(node0, node7))

