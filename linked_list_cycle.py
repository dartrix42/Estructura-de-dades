class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    vist = set() 
    
    while head is not None:
        if head in vist:
            return True
        vist.add(head.val)
        head = head.next
    return False
