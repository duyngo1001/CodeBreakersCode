    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        for _ in range(n):
            second = second.next
        while second:
            if not second.next:
                first.next = first.next.next
            first, second = first.next, second.next
        return dummy.next   
