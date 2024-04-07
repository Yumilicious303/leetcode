#Remove Nth Node From End of List
def removeNthFromEnd(head, n):
    if head is None:
        return None
    
    leader = head
    follower = head
    prev = None
    next = follower.next
    for i in range(n):
        leader = leader.next
    
    while leader:
        leader = leader.next
        prev = follower
        follower = next
        next = next.next
    
    if follower == head:
        return next
    else:
        prev.next = next
    return head