# Set approach
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    test = set()
    while headA:
        test.add(headA)
        headA = headA.next
    while headB:
        if headB in test:
            return headB
        headB = headB.next
    return None

# stuck on 2 pointer approach
'''
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    # boolean to signal one of the linked list reached the end
    end = False
    first = headA
    second = headB
    while first or second:
        if not first:
            if end:
                return None
            first = headB
            end = True
        elif not second:
            if end:
                return None
            second = headA
            end = True
        if first is second:
            return first
        first = first.next
        second = second.next
    return None
'''        
